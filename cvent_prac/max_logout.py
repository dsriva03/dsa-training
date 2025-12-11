"""
Count How Many Points Fall Inside Any Active Interval**
You are given two things:

A list of intervals representing when a machine was ON
Example: [[2, 5], [7, 10]]

A list of timestamps (points in time) when someone checked the machine:
Example: [1, 2, 3, 7, 9, 11]

Return how many checks happened while the machine was ON.
"""

def machine_checks(events, timestamps):
    #res 
    res = []
    #iterate through events 
    for start, end in events:
        for time in timestamps:
            if start <= time < end:
                res.append(time)
        #check if timestamps fall in interval, add to res
    
    #return res
    return len(res)

def machine_checks_sweep(events, timestamps):
    arr = []
    for start, end in events:
        arr.append((start, +1))
        arr.append((end, -1))
    
    arr.sort()
    print(f"{arr} when event intervals sorted")

    on_count = 0 #accumulate ONs
    time_count = 0
    i = 0 #loop over events
    j = #loop over timestamps

    while i < len(events):
        while j < len(timestamps):
            #if the event has happened before the timestamp, timestamp must be the same as event (on or off) - so update timestamp to be event[i][1] (count) and then check if its greater than zero(on)
            if timestamps[j] > events[i][0]:
                time_count += events[i][1]

                if time_count > 0:
                    on_count += 1
            
            i += 1
            j += 1

    
    return on_count





print(machine_checks_sweep([[1,3], [2,4], [5,9]], [1,2,3,4]))
