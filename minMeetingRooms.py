class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        return min_meeting_rooms(intervals)       
        #sort by starting time and ending time independently
        #start time is room +1, end time is room -1
        #return max number of concurrent rooms
        #I think is the same O(n log n ) time complexity, space complexity at O(n)

def min_meeting_rooms(intervals):
    start = [interval[0] for interval in intervals]
    end = [interval[1] for interval in intervals]
    start.sort()
    end.sort()
    start_p, end_p, max_rooms, rooms = 0, 0, 0, 0
    while start_p  < len(start):
        if start[start_p]  < end[end_p]:
            rooms += 1
            start_p += 1
        else:
            rooms -= 1
            end_p += 1
        max_rooms = max(max_rooms, rooms)
    return max_rooms