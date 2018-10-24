from pymath.number_theory.number_types import *


def test_is_even():
    assert is_even(2)
    assert is_even(0)
    assert not is_even(1)
    assert not is_even(-1)


def test_is_prime():
    assert is_prime(101)
    assert not is_prime(0)
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(7)
    assert is_prime(-7)


def test_is_mersenne_prime():
    assert is_mersenne_prime(3)
    assert not is_mersenne_prime(4)
    assert not is_mersenne_prime(11)


def test_is_perfect():
    assert is_perfect(6)
    assert not is_perfect(5)
    assert not is_perfect(1)


def test_is_regular():
    assert is_regular(48)
    assert is_regular(75)
    assert not is_regular(14)


def test_is_highly_composite():
    assert is_highly_composite(60)
    assert not is_highly_composite(59)
    assert not is_highly_composite(3)
    assert is_highly_composite(2)
    assert is_highly_composite(1)


def test_is_largely_composite():
    assert is_largely_composite(60)
    assert not is_largely_composite(5)
    assert is_largely_composite(3)
    assert is_largely_composite(2)
    assert is_largely_composite(1)
