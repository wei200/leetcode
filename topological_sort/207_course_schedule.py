class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        # Topological sort
        
        # O(V+E) since In step âdâ, each task can become a source only once and each edge (prerequisite) will be accessed and removed once. 
        # O(v+E)  since we are storing all of the prerequisites for each task in an adjacency list.
        
        # initialize the graph
        result = []
        
        # a. initilaize the graph
        
        count_in_edges = {i: 0 for i in range(numCourses)}  # count of imcoming edges for each vertex
        graph = {i: [] for i in range(numCourses)} # adjacency list graph
        
        # b. build the graph
        for edge in prerequisites:
            parent, child = edge[0], edge[1]
            graph[parent].append(child)
            count_in_edges[child] += 1
        
        # c. find all souces i.e. all vertices with 0 incoming degree
        sources = deque()
        for key in count_in_edges:
            if count_in_edges[key] == 0:
                sources.append(key)
                
        # d.
        while sources:
            vertex = sources.popleft()
            result.append(vertex)
            for child in graph[vertex]:
                count_in_edges[child] -= 1
                if count_in_edges[child] == 0:
                    sources.append(child)
                    
        return len(result) == numCourses
        
        
        
