class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return (map(list,zip(*matrix)))