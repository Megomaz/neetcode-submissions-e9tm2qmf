class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        count = 0

        for i,interval in enumerate(intervals):
            if i == 0:
                continue
            
            prev_start,prev_end = intervals[i-1]
            start,end = interval

            if prev_end > start:
                intervals[i] = (min(start,prev_start), min(end, prev_end))
                count += 1
        return count