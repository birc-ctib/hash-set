"""Testing set implementations."""

from interface import SetCons
from hashset import HashSet
from hashset2 import HashSet2


def check_set(set_type: SetCons) -> None:
    """Test that we have an implementation of a set."""
    x = list(range(10))
    s = set_type(x)
    assert s

    for a in x:
        assert a in s
        s.remove(a)
        assert a not in s

    assert not s

    for a in x:
        s.add(a)
    for a in x:
        assert a in s
        s.remove(a)
        assert a not in s


def test_builtin() -> None:
    """Test builtin set."""
    check_set(set)


def test_hash_set() -> None:
    """Test builtin set."""
    check_set(HashSet)


def test_hash_set2() -> None:
    """Test builtin set."""
    check_set(HashSet2)
