"""Utility: retry."""

def retry(fn, times=3):
    for i in range(times):
        try: return fn()
        except Exception as e:
            if i==times-1: raise
