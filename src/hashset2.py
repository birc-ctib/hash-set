"""Hash table implementation of a set."""

from typing import (
    Generic, Iterable, TypeVar, Iterator
)

Key = int
Val = TypeVar('Val')


class HashSet2(Generic[Val]):
    """Set implementation using a hash table."""

    size: int
    used: int
    array: list[list[tuple[Key, Val]]]

    def __init__(self, seq: Iterable[Val] = (), initial_size: int = 16):
        """Create a set from a sequence, optionally with a specified size."""
        seq = list(seq)

        if 2 * len(seq) > initial_size:
            initial_size = 2 * len(seq)

        self.size = initial_size
        self.used = 0
        self.array = [list() for _ in range(initial_size)]

        for value in seq:
            self.add(value)

    def _get_bin(self, k: Key) -> list[tuple[Key, Val]]:
        """Get the list (bin) that element should sit in."""
        return self.array[k % self.size]

    def _bin_contains(self, k: Key, v: Val) -> bool:
        """Test if the k bin contains v."""
        for kk, vv in self._get_bin(k):
            if k == kk:
                return v == vv
        return False

    def _resize(self, new_size: int) -> None:
        """Change the table size to new_size bins."""
        old_array = self.array
        self.size = new_size
        self.used = 0
        self.array = [list() for _ in range(new_size)]
        for b in old_array:
            for k, v in b:
                self._add(k, v)

    def _add(self, k: Key, v: Val) -> None:
        """Add element to the set."""
        if not self._bin_contains(k, v):
            self._get_bin(k).append((k, v))
            self.used += 1
            if self.used > self.size / 2:
                self._resize(int(2 * self.size))

    def add(self, element: Val) -> None:
        """Add element to the set."""
        self._add(hash(element), element)

    def _remove(self, k: Key, v: Val) -> None:
        """Remove element from the set."""
        if not self._bin_contains(k, v):
            raise KeyError(v)
        self._get_bin(k).remove((k, v))
        self.used -= 1
        if self.used < self.size / 4:
            self._resize(int(self.size / 2))

    def remove(self, element: Val) -> None:
        """Remove element from the set."""
        self._remove(hash(element), element)

    def __iter__(self) -> Iterator[Val]:
        """Iterate through all the elements in the set."""
        for b in self.array:
            for _, v in b:
                yield v

    def __bool__(self) -> bool:
        """Test if the set is non-empty."""
        return self.used > 0

    def __contains__(self, element: Val) -> bool:
        """Test if element is in the set."""
        return self._bin_contains(hash(element), element)

    def __repr__(self) -> str:
        """Get representation string."""
        return 'HashTableSet(' + repr(tuple(self)) + ')'
