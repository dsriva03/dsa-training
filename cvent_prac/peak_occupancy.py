"""
You are given a list of intervals representing when each person was inside a store.

Each interval is a pair [enter_time, exit_time], where:

enter_time = the time a person enters the store

exit_time = the time the same person leaves the store

All times are integers.

Return the maximum number of people that were inside the store at the same time.
"""

def peak_occ(events):
    arr = []
    #split events into time, count_of_person
    for start, end in events:
        arr.append((start, +1))
        arr.append((end, -1))

    #sort events 
    arr.sort()
    #keep track of people in stores with same times
    max_count = 0
    curr_count = 0
    for time, count in arr:
        curr_count += count
        max_count = max(max_count, curr_count)
    
    return max_count


    
