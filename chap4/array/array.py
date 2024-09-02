import random

arr: list[int] = [0] * 5
nums: list[int] = [1, 3, 2, 5, 4]

def random_access(nums: list[int]) -> int:
    random_index = random.randint(0, len(nums) - 1)
    random_num = nums[random_index]
    return random_num

def insert(nums: list[int], num: int, index: int):
    for i in range(len(nums) - 1, index, -1):
        nums[i] = nums[i - 1]
    nums[index] = num

def remove(nums: list[int], index: int):
    for i in range(index, len(nums) - 1):
        nums[i] = nums[i + 1]

def traverse(nums: list[int]):
    count = 0
    for i in range(len(nums)):
        count += nums[i]
    for num in nums:
        count += num
    for i , num in enumerate(nums):
        count += nums[i]
        count += num
        print(i, num)

def find(nums: list[int], target:int) -> int:
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

def extend(nums: list[int], enlarge: int) -> list[int]:
    res = [0] * (len(nums) + enlarge)
    for i in range(len(nums)):
        res[i] = nums[i]
    return res

if __name__ == "__main__":
    random_res = random_access(nums)
    print(f"random access result: {random_res}")

    insert(nums, 6, 3)
    print(f"insert result: {nums}")

    remove(nums, 2)
    print(f"remove result: {nums}")

    traverse(nums)

    find_res = find(nums, 3)
    print(f"find result: {find_res}")

    nums = extend(nums, 10)
    print(f"extend result: {nums}")