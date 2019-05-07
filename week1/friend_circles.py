
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        
        
        circles = 0
        visited = set()
        for person in range(len(M)):
            if person not in visited:
                circles += 1
                self.dfs(person, M, visited)
                
        return circles
            
            
    def dfs(self, node, M, visited):
        for person, is_friend in enumerate(M[node]):
            if is_friend and person not in visited:
                visited.add(person)
                self.dfs(person, M, visited)
                
