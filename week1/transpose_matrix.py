class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        r = len(A)
        result = [[None] * r for _ in range(len(A[0]))]
        for row_num , inner_list in enumerate(A):
            for indx, val in enumerate(inner_list):
                result[indx][row_num] = val

        return result
