import random
from typing import TypeVar, Callable, Iterable
from collections import deque
T = TypeVar('T')


def emerge_sort(
        data: Iterable[T],
        cmp: Callable,
        n_distinct: int = 1,
):
    """
    Perform an emerge Sort — a variant of merge sort designed to reduce memory locality and encourage cold-start comparisons.

    Parameters
    ----------
    data : Iterable[T]
        The input sequence of items to be sorted.

    cmp : Callable
        A binary comparison function that returns a negative number if the first argument is less than the second.

    n_distinct : int, optional
        rolling window of size.

    Returns
    -------
    List[T]
        A new list containing the sorted items.

    Notes
    -----
    This is a beta version of the Emerge Sort algorithm. It is intended primarily for experimental use.

    """
    arr = list(data)
    assert n_distinct >= 1, "n_distinct must be at least 1"
    if len(arr) < (n_distinct + 1) * 2 + 1:
        raise ValueError(
            "The length of the array must be at least (n_distinct + 1) * 2 + 1"
        )

    last_accessed = [0] * len(arr)
    counter = 1

    def do_cmp(left: int, right: int) -> int:
        # Update the access and counter
        nonlocal counter
        last_accessed[left] = counter
        last_accessed[right] = counter
        counter += 1

        # Compare the elements
        return cmp(arr[left], arr[right])

    # prepare the array for merging
    to_merge: deque[tuple[deque[int], deque[int], deque[int]]] = deque()
    unpaired: deque[int] | None = None
    for i in range(len(arr) // 2):
        to_merge.append(
            (deque([2 * i]), deque([2 * i + 1]), deque()))
    if len(arr) % 2 == 1:
        unpaired = deque([len(arr) - 1])

    # keep merge
    while not (len(to_merge) == 0):
        pair = to_merge[0]
        left, right, merged = pair

        # if either left or right are recently accessed, compare randomly
        l_access = last_accessed[left[0]]
        r_access = last_accessed[right[0]]
        recent = counter - n_distinct
        if (l_access >= recent and l_access != 0) or (r_access >= recent and r_access != 0):
            options = [i for i in
                       range(len(arr)) if last_accessed[i] < counter - n_distinct
                       ]
            assert len(options) >= 2, "Not enough distinct elements to compare"
            do_cmp(*random.sample(options, 2))
            continue

        to_merge.popleft()
        if do_cmp(left[0], right[0]) <= 0:
            merged.append(left.popleft())
        else:
            merged.append(right.popleft())

        if len(left) != 0 and len(right) != 0:
            # put back
            to_merge.append((left, right, merged))
            continue

        # finish merging the pair
        if len(left) == 0:
            merged.extend(right)
        else:
            merged.extend(left)

        # put back
        if unpaired is not None:
            paired = (merged, unpaired, deque())
            unpaired = None
            to_merge.append(paired)
        else:
            unpaired = merged

    assert unpaired is not None, "unpaired should not be None"

    return [arr[i] for i in unpaired]  # convert indices back to values


def ascending_cmp(x: int, y: int) -> int:
    """A simple ascending comparison function.

    Note
    ----
    You should implement a custom comparison function to ask participants to provide each comparison result.
    """

    return (x > y) - (x < y)


if __name__ == "__main__":
    # Example usage
    data = [5, 3, 8, 6, 2, 7, 4, 1]
    sorted_data = emerge_sort(data, ascending_cmp, n_distinct=2)
    print("Sorted data:", sorted_data)
    assert sorted_data == sorted(
        data), "The emerge_sort did not sort the data correctly."
