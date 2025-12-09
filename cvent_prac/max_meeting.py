"""
🌟 SWEEP LINE PROBLEM #2: Count the Maximum Number of Meetings Happening at the Same Time

You are given a list of meetings.
Each meeting has a start time and end time:

[ [start1, end1], [start2, end2], ... ]


Return the maximum number of meetings happening simultaneously.

"""


arr = []

def max_meeting(meetings):
    for start, end in meetings:
        arr.append((start, +1))
        arr.append((end, -1))
    
    arr.sort()

    curr_c = 0
    max_c = 0

    for time, count in arr:
        curr_c += count
        max_c = max(max_c, curr_c)
    
    return max_c


