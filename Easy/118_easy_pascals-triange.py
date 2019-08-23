class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        soln = [[1], [1,1]]
        if numRows <= 2:
            return soln[:numRows]
        i = 2
        while i < numRows:
            prev = soln[i-1]
            curr = [prev[0]]
            for j in range(len(prev)):
                if j == len(prev) - 1:
                    curr.append(prev[j])
                else:
                    curr.append(prev[j] + prev[j+1])
            soln.append(curr)
            i += 1
        return soln