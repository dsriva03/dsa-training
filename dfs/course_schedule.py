def course_schedule_dfs(numCourses, prerequisites):

    #build adj. list
    graph = {}

    for i in range(numCourses):
        graph[i] = []
    
    for a, b in prerequisites:
        graph[b].append(a) #


    #build seen as array
    seen = [0] * numCourses

    #dfs on course
    def dfs(course):
        #if cycle, return False
        if seen[course] == 1:
            return False
        #mark course as visiting (1)
        seen[course] = 1

        #call dfs on nei, if False, bubble up False
        for nei in graph[course]:
            if not dfs(nei):
                return False

        #update course to 2 (visited)
        seen[course] = 2
        #return True
        return True
    
    for i in range(numCourses):
        if not dfs(i):
            return False
    
    return True

        