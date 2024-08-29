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

if __name__ == "__main__":
    random_res = random_access(nums)
    print(f"random access result: {random_res}")

    insert(nums, 6, 3)
    print(f"insert result: {nums}")