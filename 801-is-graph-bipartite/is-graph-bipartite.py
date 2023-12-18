class Solution:
    def isBipartite(self, adj: List[List[int]]) -> bool:
        #code here
        a = set()
        b = set()
        traversed = set()
        def dfs(key, key_set):
            if key in traversed:
                return
            else:
                traversed.add(key)
            l = adj[key]
            if key_set == "a":
                for item in l:
                    b.add(item)
                    # traversed.add(item)
                    if item not in traversed:
                        dfs(item, "b")
            else:
                for item in l:
                    a.add(item)
                    if item not in traversed:
                        dfs(item, "a")
        # print(graph)           
        for i in range(len(adj)):
            
            if i in a and i in b:
                return False
            if i not in a and i not in b:
                a.add(i)
                dfs(i,"a")
        # traversed.add(0)
        print(a,b)
        if len(a.intersection(b)) > 0:
            return False
        return True