# 📘 Assignment: Search Algorithms — Linear vs Binary

## 🎯 Objective

Implement and compare two fundamental search algorithms: linear search and binary search. Learn when each algorithm applies and compare their behavior on small lists.

## 📝 Tasks

### 🛠️ Implement `linear_search` and `binary_search`

#### Description
Write two functions with the following signatures:

- `def linear_search(arr: list, target: int) -> int`
- `def binary_search(arr: list, target: int) -> int`

Each function should return the index of `target` in `arr` or `-1` if not found. `binary_search` assumes `arr` is sorted in ascending order.

#### Requirements
Completed code should:

- Correctly find an element's index or return `-1` when missing.
- `binary_search` must use an iterative or recursive divide-and-conquer approach.
- Include brief examples or tests showing both functions on small lists.

### 🛠️ Compare behavior

#### Description
Run both searches on the same inputs (sorted list) and note differences in number of comparisons and when `binary_search` is more efficient.

#### Requirements

- Show at least three example cases: target at start, middle, and not present.
- Explain in one sentence when to prefer each algorithm.

## Stretch Goal

- Modify `binary_search` to return the index where the target should be inserted to keep the list sorted (i.e., implement a `bisect`-style behavior).
