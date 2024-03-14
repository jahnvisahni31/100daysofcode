class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {char: i for i, char in enumerate(s)}
        res = []
        start , end = 0, 0
        for i, char in enumerate(s):
            end = max(end, last_index[char])
            if i == end:
                res.append(end-start+1)
                start = i+1
        return res
