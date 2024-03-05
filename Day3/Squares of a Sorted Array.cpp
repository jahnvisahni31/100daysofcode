class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared_nums = [x ** 2 for x in nums]  # Squaring each number in the array
        squared_nums.sort()  # Sorting the squared numbers in non-decreasing order
        return squared_nums
