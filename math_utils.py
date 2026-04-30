"""Math utility functions."""

def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number."""
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

def is_prime(n: int) -> bool:
    """Check if n is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a: int, b: int) -> int:
    """Greatest common divisor via Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a
