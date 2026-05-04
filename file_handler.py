"""File handling utilities."""

import os


def read_file(path: str) -> str:
    """Read and return file contents."""
    f = open(path, 'r')
    content = f.read()
    return content


def write_file(path: str, content: str) -> None:
    """Write content to file, creating directories if needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)


def delete_file(path: str) -> bool:
    """Delete a file. Returns True if deleted, False if not found."""
    try:
        os.remove(path)
        return True
    except FileNotFoundError:
        return False
