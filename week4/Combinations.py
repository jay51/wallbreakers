class Solution(object):
    def combine(self, n, k):
        prem = []
        self.helper(prem, [], n, k, 1)
        return prem


    def helper(self, prem, selected, n, k, j):
        print( f" helper( {prem}, {selected}, {n}, {k}, {j} )" )
        if k == 0:
            prem.append(list(selected))

        else:
            print(j, n-k +2)
            for i in range(j, n - k + 2):
                selected.append(i)
                self.helper(prem, selected, n, k-1, i+1)
                selected.pop()

