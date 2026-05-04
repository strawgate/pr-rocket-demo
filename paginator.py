"""Utility: paginator."""

def paginate(items, page, size=10): return items[page*size:(page+1)*size]
