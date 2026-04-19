<!-- Phase 1: Direct enumerate() Usage (Foundation)

These force you to use enumerate() correctly.

1. Find First Occurrence

Prompt

def find_index(nums, target):
    # return index of target or -1

Constraint

Must use enumerate()

What this trains

index + value pairing
2. Print Even Index Values

Prompt

nums = [10, 15, 20, 25, 30]

# print values at even indexes only

What this trains

using index from enumerate() for filtering
3. Build Index Map

Prompt

def build_index_map(nums):
    # return {value: index}

Example

[4, 7, 1] → {4:0, 7:1, 1:2}

What this trains

hash map + enumerate (CORE DSA PATTERN)
4. Find All Matching Indexes

Prompt

def find_all_indexes(nums, target):
    # return list of all indexes where target appears

What this trains

collecting multiple positions
Phase 2: Real DSA Patterns (Critical)

Now you apply enumerate() inside real patterns.

5. Contains Duplicate

Prompt

def contains_duplicate(nums):
    # return True if any value appears twice

Constraint

Use a set
Use enumerate() (even if not strictly required)

What this trains

membership checks + iteration 


6. Two Sum (MUST MASTER)

Prompt

def two_sum(nums, target):
    # return indices of two numbers that add up to target

Constraint

Must use enumerate()
Must use a dictionary

What this trains

hashmap + index tracking (TOP 5 pattern)

7. First Unique Character (String)

Prompt

def first_unique_char(s):
    # return index of first non-repeating character

What this trains

Counter + enumerate()
string as array

Phase 3: Force Decision (enumerate vs range)

Now you must decide which to use.

8. Reverse Array In-Place

Prompt

def reverse(nums):
    # modify list in place

Hint

You need swapping

Correct choice

range(len()) or two pointers
NOT enumerate()

9. Maximum Profit (Stock Problem)

Prompt

def max_profit(prices):
    # buy low, sell high once

Hint

track min price and profit

Decision

either works, but enumerate() is cleaner

10. Palindrome Check

Prompt

def is_palindrome(s):
    # return True if string is palindrome

Hint

compare left and right

Correct choice

range(len()) (index math required)
Phase 4: Debugging (High Value Skill)

These expose mistakes.

# 2. Python Built-ins (LeetCode essentials)

You don’t need all built-ins. You need the **high-leverage ones**.

---

## A. Iteration + Structure

### `len()`

```python
len(nums)
```

Used everywhere. O(1).

---

### `range()`

```python
for i in range(len(nums)):
```

Used when:

* you need index only
* or sliding window

---

### `enumerate()` ✅ (already covered)

---

## B. Collections (VERY IMPORTANT)

### `set()`

Fast lookups (O(1))

```python
nums = [1, 2, 3]
seen = set(nums)

if 2 in seen:
    print("yes")
```

Use case:

* duplicates
* membership checks

---

### `dict()` (hash map)

```python
d = {}
d["a"] = 1
```

Use case:

* frequency count
* index tracking
* caching results

---

### `collections.Counter`

```python
from collections import Counter

s = "aabbc"
count = Counter(s)
```

Output:

```
{'a': 2, 'b': 2, 'c': 1}
```

Use case:

* string frequency problems

---

## C. Useful Helpers

### `sorted()`

```python
sorted(nums)
```

Used for:

* comparing anagrams
* ordering data

---

### `sum()`

```python
sum(nums)
```

---

### `max()` / `min()`

```python
max(nums)
min(nums)
```

---
-->

### `zip()`

```python
a = [1,2]
b = [3,4]

for x, y in zip(a, b):
    print(x, y)
```

