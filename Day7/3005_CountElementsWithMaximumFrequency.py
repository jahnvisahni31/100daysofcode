class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        frq = Counter(nums)
        max_fre = max(frq.values())
        max_e = [num for num , frqw in frq.items() if frqw == max_fre]
        to = sum([frqw for num, frqw in frq.items() if num in max_e])
        return to
