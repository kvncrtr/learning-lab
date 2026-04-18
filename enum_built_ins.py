# Enumerate Method + Built In Methods
# git add .; git commit; git push;

# # Learn Enumerate Method
# nums = [10, 20, 30, 40, 50]

# for index, value in enumerate(nums):
#     print(f"""
#     Printed Index: {index}
#     Printed Value: {value}
#     """)

# # Enums for DSA Practice
# # 1-1 Find First Occurance
# def find_index(nums, target):
#     for i, val in enumerate(nums):
#         if val == target:
#             return i
#     return -1

# result = find_index(nums, 90)
# print(result)

# # 1-2 Print Evens
# nums_0 = [10, 15, 20, 25, 30]

# for i, val in enumerate(nums_0):
#     if i % 2 == 0:
#         print(val)

# # 1-3 Build an Index Map
# nums_1 = [10, 15, 20, 25, 30]

# def build_index_map(nums_1):
#     # {key: value for item in iterable}
#     return {val: i for i, val in enumerate(nums_1)}
#     # index_map = {}
#     # for i, val in enumerate(nums_1):
#     #     index_map[val] = i
    
#     # return index_map

# result = build_index_map(nums_1)
# print(result)

# # 1-4 Find All Matching Indexes
# nums_2 = [10, 15, 20, 10, 20, 30, 40, 50, 25, 30, 10, 20, 30, 40, 50, 10, 15, 20, 25, 30, 10, 15, 20, 25, 30]
# def find_all_indexes(nums, target):
#     # [expression for item in iterable if condition]
#     # “Build a list of THIS… from THIS LOOP… under THIS CONDITION”
#     return [i for i, val in enumerate(nums) if val == target]
#     # matches = []
#     # # return list of all indexes where target appears
#     # for i, val in enumerate(nums):
#     #     if target == val:
#     #         matches.append(i)
#     # return matches

# print(find_all_indexes(nums_2, 30))

# # 1-5 Find Dups
# nums_3 = [7, 2, 9, 4, 7, 6, 2, 8, 5]

# def contains_duplicate(nums):
#     seen = set()

#     for i, val in enumerate(nums):
#         if val in seen:
#             return True
#         seen.add(val)
#         print(seen)
#     # return False

# result = contains_duplicate(nums_3)
# print(result)

# # 1-6 Two Sum
# # return number of UNIQUE pairs that sum to target
# nums_4 = [1, 3, 2, 2, 4, 0, 5, 3]

# def two_sum(nums, target):
#     seen = set()
#     pairs = set()

#     for i, val in enumerate(nums):
#         comp = target - val

#         if comp in seen:
#             pair = tuple(sorted((val, comp)))
#             pairs.add(pair)

#         seen.add(val)

#     return len(pairs)
        
# result = two_sum(nums_4, 5)
# print(result)

# # 1-7. First Unique Character (String)
# # return char of first non-repeating character

# def first_unique_char(s):
#     seen = {}

#     for i, val in enumerate(s):
#         if val not in seen:
#             seen[val] = [1, i]
#         else:
#             seen[val][0] += 1
    
#     for i, val in enumerate(s):
#         if seen[val][0] == 1:
#             return val
        
#     return -1

# print(first_unique_char('swiss'))
# print(first_unique_char('leetcode'))
# print(first_unique_char('aabbcc'))
# print(first_unique_char('cevin carter'))

# # 1-8
# # You need swapping Correct choice

# nums_5 = [1, 3, 2, 2, 4, 0, 5, 3]
# left = 0
# right = len(nums_5) - 1

# while left < right:
#     nums_5[left], nums_5[right] = nums_5[right], nums_5[left]
#     left += 1
#     right -= 1

# print(nums_5)

# # 1-9
# # Maximum Profit (Stock) Buy once, sell once → maximize profit
# prices = [300, 500, 11000, 7000, 2000]

# def max_profit(prices):
#     min_price = prices[0]
#     max_price = 0

#     for i, val in enumerate(prices):
#         if val < min_price:
#             min_price = val
#         else:
#             profit = val - min_price
#             max_profit = max(max_profit, profit)

#     return max_price - min_price

# roi = max_profit(prices)
# print(roi)

# # 1-10 Is Palindrome Check
# def is_palindrome_check(s):
#     left = 0
#     right = len(s) - 1
#     rev_str = ''

#     for i, val in enumerate(s):
#         print(val, rev_str)
#         rev_str = val + rev_str
        
#     if rev_str == s:
#         return True
    
#     return False

# print(is_palindrome_check('koren'))

# Built-In Methods racecar
# print(len(nums))