def insertInterval(intervals, newInterval):

    res = []

    for start, end in intervals:
        if end < newInterval[0]:
            res.append([start, end])
    #if current interval is completely before new, append it to res
        elif newInterval[1] < start:
            res.append(newInterval)
    #if current is completely after new, append new, and update new to current
            newInterval = [start, end]

    #otherwise they are overlapping, so we merge
        else:
            newInterval[0] = min(start, newInterval[0])
            newInterval[1] = max(end, newInterval[1])

    res.append(newInterval)
    #append new to res, whatever the final form is
    return res