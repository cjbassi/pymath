import math
from functools import reduce
from math import log
from typing import Iterator, List, Tuple

from . import number_types


def factors(n: int) -> Iterator[int]:
    n = abs(n)
    return (i for i in range(1, n+1) if n % i == 0)


def lcm(a: int, *terms: int) -> int:
    def lcm_impl(a: int, b: int) -> int:
        return a * b // math.gcd(a, b)
    return reduce(lcm_impl, [a] + list(terms))


def gcd(a: int, *terms: int) -> int:
    return reduce(math.gcd, [a] + list(terms))


def extended_lcm(a: int, *terms: int) -> List[int]:
    _lcm = lcm(a, *terms)
    return [_lcm] + list(map(lambda a: _lcm // a, [a] + list(terms)))


def extended_gcd(b: int, a: int) -> Tuple[int, int, int]:
    x0, x1, y0, y1 = 1, 0, 0, 1
    while a != 0:
        q, b, a = b // a, a, b % a
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return b, x0, y0


def prime_factors(n: int) -> Iterator[int]:
    i = 2
    while i * i <= n:
        if n % i != 0:
            i += 1
        else:
            n //= i
            yield i
    if n > 1:
        yield n


def largest_prime_factor(n: int) -> int:
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n


def are_coprime(a: int, b: int, *terms: int) -> bool:
    return reduce(math.gcd, [a] + [b] + list(terms)) == 1


def phi(n: int) -> int:
    """Returns |{x in N : x < n and x coprimes to n}|."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    if number_types.is_prime(n):
        return n-1
    if log(n, 2).is_integer():
        return n // 2
    return sum(1 for i in range(1, n) if math.gcd(n, i) == 1)


def coprimes(n: int) -> Iterator[int]:
    """Returns {x in N : x < n and x coprime to n}."""
    if number_types.is_prime(n):
        return iter(range(1, n))
    if log(n, 2).is_integer():
        return iter(range(1, n, 2))
    return (i for i in range(1, n) if math.gcd(n, i) == 1)