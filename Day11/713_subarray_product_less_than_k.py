class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        c = 0
        p = 1
        le = 0
        for ri, num in enumerate(nums):
            p *= num
            while p >= k:
                p /= nums[le]
                le += 1
            c += ri -le +1
        return c
