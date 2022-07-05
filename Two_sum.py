# Two sum problem 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i, n in enumerate(nums):
            j = target - n
            if j not in diff:
                diff[n] = i
            else:
                return [diff[j], i]    
        