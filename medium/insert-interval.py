class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start,end = newInterval
        l,r = [],[]
        for curr_start, curr_end in intervals:
            if start > curr_end:
                l.append([curr_start,curr_end])
            elif end < curr_start:
                r.append([curr_start,curr_end])
            else:
                start = min(start, curr_start)
                end = max(end, curr_end)

        res = l + [[start,end]] + r
        return res
