def max_occupancy(events):
    sorted_events = sorted(event, key=lambda x: x[0])

    global_max = 0
    running_max = 0

    for i in range(len(sorted_events)):
        running_max += sorted_events[i][1]
        global_max = max(global_max, running_max)
    
    return global_max

