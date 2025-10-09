def merge_intervals(intervals:list[int]) -> list[int]:

    #sort intervals by key=startpoint
    intervals.sort(key=lambda x: x[0])

    #make res arr - populate res with interval[0]
    res = [intervals[0]]

    #iterate thru intervals and start at intervals[1]
    for start, end in intervals[1:]:

        #check if interval[1][0] is <= res[-1][1]
        if start <= res[-1][1]:
            res[-1][1] = max(end, res[-1][1])
            #overlap, so merge and update endpoint with max(endpoints)
        else:
            res.append([start, end])
        #append interval
    
    #return res
    return res
