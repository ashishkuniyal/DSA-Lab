class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        for num in set(nums):
            if nums.count(num)%2!=0:
                return False
        return True
        