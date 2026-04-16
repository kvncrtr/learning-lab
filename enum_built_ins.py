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














# Built-In Methods
# print(len(nums))