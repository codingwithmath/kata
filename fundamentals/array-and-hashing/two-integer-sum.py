from typing import List


#bruteforce
def twoSum1(nums: List[int], target: int) -> List[int]:
    i = 0

    while i < len(nums):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            
        i += 1

#using hashmap
def twoSum(nums: List[int], target: int) -> List[int]:
    prevNums = {} #value: index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevNums:
            return [prevNums[diff], i]
        
        prevNums[n] = i
    
    return

print(twoSum([14, 20, 30, 6], 50))
