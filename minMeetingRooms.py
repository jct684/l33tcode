import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        return min_meeting_rooms(intervals)
        #sort based on start times
        #store end time in a min heap
        #use min heap to determine if a meeting room is open, otherwise add to heap
        #size of heap gives us the number of required rooms
        
def min_meeting_rooms(intervals):
    sorted_intervals = sorted(intervals, key= lambda x:x[0])
    heap_m = [sorted_intervals[0][1]]
    for i in range(1, len(sorted_intervals)):
        if sorted_intervals[i][0] < heap_m[0]:
            heapq.heappush(heap_m, sorted_intervals[i][1])
        else:
            heapq.heapreplace(heap_m, sorted_intervals[i][1])
    return len(heap_m)