class Solution(object):
    def matrixReshape(self, mat, r, c):
        if r*c != len(mat)*len(mat[0]):
            return mat
        
        d1 = collections.deque(sum(mat,[]))
        
        return [[d1.popleft() for i in range(c)] for j in range(r)]
