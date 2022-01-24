class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        # Topological sort
        
        result = []
        
        # initalize the graph
        incoming_degree = {i:0 for i in range(numCourses)}
        graph = {i: [] for i in range(numCourses)}
        
        # build the graph
        for prerequisite in prerequisites:
            parent, child = prerequisite[1], prerequisite[0]
            graph[parent].append(child)
            incoming_degree[child] += 1
        
        # find the source
        sources = deque()
        for key in incoming_degree:
            if incoming_degree[key] == 0:
                sources.append(key)
                
        # find the possible ordering using BFS
        
        while sources:
            vertex = sources.popleft()
            result.append(vertex)
            for child in graph[vertex]:
                incoming_degree[child] -= 1
                if incoming_degree[child] == 0:
                    sources.append(child)
                    
        # check if there is a cycle
        if len(result) != numCourses:
            return []
        
        return result
        
