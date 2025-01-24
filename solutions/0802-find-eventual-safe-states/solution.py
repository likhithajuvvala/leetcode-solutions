class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        # 0: unvisited, 1: unsafe, 2: safe
        state = [0] * n
        
        def dfs(node):
            # If we've already determined the state of this node, return its state
            if state[node] != 0:
                return state[node] == 2
            
            # Mark the node as being visited in the current path
            state[node] = 1
            
            # Check all neighbors
            for neighbor in graph[node]:
                # If any neighbor is unsafe or leads to an unsafe node, this node is unsafe
                if not dfs(neighbor):
                    return False
            
            # If we've checked all neighbors and found no unsafe paths, mark as safe
            state[node] = 2
            return True
        
        # Find safe nodes
        safe_nodes = []
        for node in range(n):
            if dfs(node):
                safe_nodes.append(node)
        
        return safe_nodes