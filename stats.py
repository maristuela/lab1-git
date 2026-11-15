def mean(values):
    if not values:
        raise ValueError("empty sequence")
    return sum(values) / len(values)


def median(values):
    """Return the median of values."""
    if not values:
        raise ValueError("empty sequence")
    s = sorted(values)
    n = len(s)
    mid = n // 2
    if n % 2:
        return s[mid]
    return (s[mid - 1] + s[mid]) / 2
