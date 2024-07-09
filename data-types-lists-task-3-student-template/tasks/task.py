from typing import List


def foo(nums: List[int]) -> List[int]:
    new_list = []
    for num in nums:
        product = 1
        for num_index in range(len(nums)):
            if num_index != nums.index(num):
                product *= nums[num_index]
        new_list.append(product)
    return new_list


print(foo([3, 2, 1]))
print(foo([1, 2, 3, 4, 5]))