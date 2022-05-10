"""Interface a set must implement."""

from typing import (
    Protocol, TypeVar, Iterable
)

T = TypeVar('T', contravariant=True)


class Set(Protocol[T]):
    """A set of elements of type T."""

    def __contains__(self, x: T) -> bool:
        """Test if x is in set."""
        ...

    def add(self, x: T) -> None:
        """Add x to the set."""
        ...

    def remove(self, x: T) -> None:
        """Remove x from the set."""
        ...


class SetCons(Protocol):
    """
    Protocol for creating sets.

    This is a bit of a hack to work around that mypy doesn't
    work well with generic protocols.

    See: https://github.com/python/typing/issues/1179
    """

    def __call__(self, it: Iterable[T]) -> Set[T]:
        """Create a new set."""
        ...
