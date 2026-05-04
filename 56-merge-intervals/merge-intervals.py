class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
    

        intervals.sort(key=lambda x: x[0])
    
        merged = []
        start, end = intervals[0]
    
        for s, e in intervals[1:]:
            if s <= end:              # overlap
                end = max(end, e)     # extend end
            else:                     # no overlap
                merged.append([start, end])
                start, end = s, e
    
        merged.append([start, end])   # add last interval
        return merged
        
        