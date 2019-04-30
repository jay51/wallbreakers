# inp = [[1,1,0],[1,0,1],[0,0,0]]
inp = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        A = [i[::-1] for i in A ]
        for row_num , inner_list in enumerate(A):
            for indx, val in enumerate(inner_list):
                if val == 0:
                    A[row_num][indx] = 1
                if val == 1:
                    A[row_num][indx] = 0

        return A

