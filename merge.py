class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort based on start of interval
        #if the start is before the previous end then extend the interval to the new end
        #otherwise create a new interval
        #O(n*log(n) + n) = O(n log(n)) time complexity
        #space complexity O(log n) to sort
        intervals.sort(key=lambda x: x[0])
        ans = [[intervals[0][0], intervals[0][1]]]
        j=0
        for i in range(1, len(intervals)):
            if intervals[i][0] <= ans[j][1]:
                ans[j][1] = max(ans[j][1], intervals[i][1])
            else:
                ans.append([intervals[i][0], intervals[i][1]])
                j += 1
        return ans