#initial list
nums1: list[int] = []
nums: list[int] = [1, 2, 3, 4, 5]
print(f"initialize list:\nnums1: {nums1}\nnums: {nums}")

#access element
num: int = nums[1]
print(f"access result: {num}")

#update elemnt
nums[1] = 0
print(f"update result: {nums[1]}")

nums.clear()
print(f"After clear result: {nums}")

nums.append(1)
nums.append(3)
nums.append(2)
nums.append(5)
nums.append(4)
print(f"After append result: {nums}")

nums.insert(3, 6)
print(f"After insert result: {nums}")

nums.pop(3)
print(f"After pop result: {nums}")

nums1: list[int] = [6, 8, 7, 9, 10]
nums += nums1
print(f"Concatenating result: {nums}")

nums.sort()
print(f"Sorting result: {nums}")
