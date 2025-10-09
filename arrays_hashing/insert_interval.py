def insert_intervals(intervals, newInterval):

    res = []

    for start, end in intervals:
    #check if newInterval is completely befoer
        if start > newInterval[1]:
            res.append(newInterval)

            newInterval = [start, end]

    #check if newInterval is overlapping
        if start < newInterval[1]:
            #merge
            res[-1][1] = max(end, res[-1][1])
            res[-1][0] = min(end, res[-1][0])

        else: 

            res.append(start, end)


    
    return res

