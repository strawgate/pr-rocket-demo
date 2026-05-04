"""HTTP middleware chain pattern."""

from typing import Any, Callable


Handler = Callable[[dict], dict]
Middleware = Callable[[dict, Handler], dict]


def compose(*middlewares: Middleware) -> Callable[[Handler], Handler]:
    """Compose middleware functions into a single handler wrapper."""
    def wrapper(handler: Handler) -> Handler:
        def composed(request: dict) -> dict:
            chain = handler
            for mw in reversed(middlewares):
                prev = chain
                chain = lambda req, _mw=mw, _prev=prev: _mw(req, _prev)
            return chain(request)
        return composed
    return wrapper


def logging_middleware(request: dict, next_handler: Handler) -> dict:
    """Log request method and path."""
    print(f"→ {request.get('method', 'GET')} {request.get('path', '/')}")
    response = next_handler(request)
    print(f"← {response.get('status', 200)}")
    return response


def auth_middleware(request: dict, next_handler: Handler) -> dict:
    """Check for authorization header."""
    if not request.get("headers", {}).get("Authorization"):
        return {"status": 401, "body": "Unauthorized"}
    return next_handler(request)


def timing_middleware(request: dict, next_handler: Handler) -> dict:
    """Add response timing header."""
    import time
    start = time.time()
    response = next_handler(request)
    response.setdefault("headers", {})["X-Response-Time"] = f"{(time.time() - start)*1000:.1f}ms"
    return response
