# Hash table set

We will not ask you to implement a complete hash table yourself, although we obviously don't think it would be a problem for such excellent students as yourself... Here is an implementation that we would like to ask you to improve, though. That implementaion can be found in `src/hashset.py`. The problem is that resizing is more expensive than it should be.

The resizing functionality looks like this:

```python
    def _resize(self, new_size: int) -> None:
        """Change the table size to new_size bins."""
        old_array = self.array
        self.size = new_size
        self.used = 0
        self.array = [list() for _ in range(new_size)]
        for b in old_array:
            for x in b:
                self.add(x)
```

Whenever we need to change the table's size, we first get hold of the old array of bins and replace it with a new of the desired size. Then we run through all the bins in it, then all the elements in a bin, and each element is inserted using `self.add(x)`. There is nothing seriously wrong with that; when calling `self.add(x)` the table is already updated with the new array and everything works correctly. However, there is one potentially expensive operation that should be avoided.

In `add()` we do this:

```python
    def add(self, element: T) -> None:
        """Add element to the set."""
        b = self._get_bin(element)  # <- Get the bin for element
```

where `_get_bin()` looks like this:

```python
    def _get_bin(self, element: T) -> list[T]:
        """Get the list (bin) that element should sit in."""
        hash_val = hash(element)  # <- computing the hash value for the element
        index = hash_val % self.size
        return self.array[index]
```

The problem is that computing the hash value, `hash(element)`, can be a costly operation. The hash value of an element should never change, (if it does, you have a big problem), so the elements we already have in my table will have the same hash value before and after resizing. If we save the hash key together with the values in the table, we don't have to compute `hash(element)` again in a resize. We still have to compute the index, `hash_val % self.size`, because `self.size` changes, but that is a fast operation compared to what `hash()` could be.

In `src/hashset2.py` there is a copy the original hash table code. Can you change it, so the bins contain pairs of keys and values, so you don't have to compute `hash(x)` when you resize? You will have to touch almost the entire implementation to handle that the values in the lists are now pairs.
