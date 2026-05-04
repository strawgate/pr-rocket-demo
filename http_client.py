"""Minimal HTTP client wrapper."""

import json
import urllib.request
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Response:
    status: int
    body: str
    headers: dict[str, str]

    def json(self) -> Any:
        return json.loads(self.body)


def get(url: str, headers: dict[str, str] | None = None, timeout: int = 30) -> Response:
    """Perform an HTTP GET request."""
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return Response(
            status=resp.status,
            body=resp.read().decode(),
            headers=dict(resp.headers),
        )


def post(url: str, data: Any, headers: dict[str, str] | None = None, timeout: int = 30) -> Response:
    """Perform an HTTP POST request with JSON body."""
    body = json.dumps(data).encode()
    h = {"Content-Type": "application/json", **(headers or {})}
    req = urllib.request.Request(url, data=body, headers=h, method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return Response(
            status=resp.status,
            body=resp.read().decode(),
            headers=dict(resp.headers),
        )
