"""Utility: validator."""

def validate_email(s): return '@' in s and '.' in s.split('@')[-1]
