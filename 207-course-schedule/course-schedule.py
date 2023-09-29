class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [0] * numCourses
        recStack = [0] * numCourses
        mapper = {}
        for p in prerequisites:
            if p[0] in mapper:
                mapper[p[0]].append(p[1])
            else:
                mapper[p[0]] = [p[1]]
        
        def detectCycle(idx, visited, recStack):
            visited[idx] = 1
            recStack[idx] = 1
            
            if idx not in mapper:
                #No cycle as no dependency
                recStack[idx] = 0
                return False
            else:
                for i in mapper[idx]:
                    if visited[i] == 0:
                        #This neighbour is not visited
                        if detectCycle(i, visited, recStack):
                            #if there is a cycle present
                            return True
                    elif recStack[i] == 1:
                        return True
            recStack[idx] = 0
            return False


        for i in range(len(prerequisites)):
            # print(i)
            if detectCycle(prerequisites[i][0], visited, recStack):
                return False
        return True

            

        
        
        