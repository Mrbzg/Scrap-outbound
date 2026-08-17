"""HTTP client with cache, retries and polite headers."""

from __future__ import annotations

import hashlib
import json
import time
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

DEFAULT_UA = (
    "Mozilla/5.0 (compatible; ScrapOutbound/1.0; +https://github.com/Mrbzg/Scrap-outbound)"
)


class HttpClient:
    def __init__(
        self,
        cache_dir: str | Path = "data/cache",
        timeout: int = 30,
        sleep_between: float = 0.8,
        use_cache: bool = True,
    ):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.timeout = timeout
        self.sleep_between = sleep_between
        self.use_cache = use_cache
        self._last_host: Optional[str] = None
        self._last_ts = 0.0

        retry = Retry(
            total=3,
            backoff_factor=1.2,
            status_forcelist=(429, 500, 502, 503, 504),
            allowed_methods=frozenset(["GET", "HEAD"]),
        )
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": DEFAULT_UA,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "es-MX,es;q=0.9,en;q=0.8",
            }
        )
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def _cache_path(self, url: str) -> Path:
        h = hashlib.sha256(url.encode("utf-8")).hexdigest()[:24]
        host = urlparse(url).netloc.replace(":", "_")
        return self.cache_dir / f"{host}_{h}.html"

    def _throttle(self, url: str) -> None:
        host = urlparse(url).netloc
        now = time.time()
        if self._last_host == host and (now - self._last_ts) < self.sleep_between:
            time.sleep(self.sleep_between - (now - self._last_ts))
        self._last_host = host
        self._last_ts = time.time()

    def get_text(self, url: str, force: bool = False) -> str:
        """Fetch URL text, using disk cache when available."""
        path = self._cache_path(url)
        if self.use_cache and not force and path.exists():
            return path.read_text(encoding="utf-8", errors="replace")

        self._throttle(url)
        text = ""
        status = 0
        last_err: Exception | None = None

        try:
            resp = self.session.get(url, timeout=self.timeout)
            resp.raise_for_status()
            if not resp.encoding or resp.encoding.lower() == "iso-8859-1":
                resp.encoding = resp.apparent_encoding or "utf-8"
            text = resp.text
            status = resp.status_code
        except requests.RequestException as exc:
            last_err = exc
            # Fallback: curl often survives flaky TLS middleboxes
            text = self._curl_fallback(url)
            if text:
                status = 200
            else:
                meta = {"url": url, "error": str(exc), "ts": time.time()}
                path.with_suffix(".error.json").write_text(
                    json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
                )
                raise

        if self.use_cache and text:
            path.write_text(text, encoding="utf-8")
            path.with_suffix(".meta.json").write_text(
                json.dumps({"url": url, "status": status, "ts": time.time()}, indent=2),
                encoding="utf-8",
            )
        return text

    def _curl_fallback(self, url: str) -> str:
        import subprocess

        try:
            proc = subprocess.run(
                [
                    "curl",
                    "-fsSL",
                    "--max-time",
                    str(self.timeout),
                    "-A",
                    DEFAULT_UA,
                    url,
                ],
                capture_output=True,
                text=True,
                timeout=self.timeout + 5,
            )
            if proc.returncode == 0 and proc.stdout:
                return proc.stdout
        except Exception:
            return ""
        return ""
