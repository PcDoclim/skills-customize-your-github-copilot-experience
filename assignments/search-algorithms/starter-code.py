"""Starter code for Search Algorithms assignment.

Students should implement `linear_search` and `binary_search`.
"""
from typing import List


def linear_search(arr: List[int], target: int) -> int:
    """Return index of target in arr or -1 if not found."""
    for i, v in enumerate(arr):
        if v == target:
            return i
    return -1


def binary_search(arr: List[int], target: int) -> int:
    """Return index of target in a sorted arr or -1 if not found."""
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def _demo():
    examples = [
        ([1, 2, 3, 4, 5], 1),
        ([1, 2, 3, 4, 5], 3),
        ([1, 2, 3, 4, 5], 9),
    ]

    for arr, target in examples:
        print(f"Array: {arr}, target: {target}")
        print("  linear_search ->", linear_search(arr, target))
        print("  binary_search ->", binary_search(arr, target))
        print()


if __name__ == "__main__":
    _demo()
