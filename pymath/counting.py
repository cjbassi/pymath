from math import factorial
from typing import Collection, Iterator, List, TypeVar

__all__ = ['Choose', 'Permute', 'powerset']

T = TypeVar('T')


def Choose(n: int, k: int) -> int:
    return factorial(n) // (factorial(n - k) * factorial(k))


def Permute(n: int, k: int) -> int:
    return factorial(n) // (factorial(n - k))


def powerset(collection: Collection[T]) -> Iterator[List[T]]:
    def powerset_impl(seq):
        if len(seq) == 0:
            yield []
        else:
            for item in powerset(seq[1:]):
                yield item
                yield [seq[0]] + item
    return powerset_impl(list(collection))
