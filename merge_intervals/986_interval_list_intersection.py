class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        # O(len(A)+len(B))
        # O(1)
        result = []
        i,j = 0,0
        start = 0
        end = 1
        
        while i < len(A) and j < len(B):
            # check if intervals overlap and A[i]'s start time lies within other B[j]
            a_overlap_b = A[i][start] >= B[j][start] and A[i][start] <= B[j][end]
            
            # check if intervals overlap and A[j]'s start time lies with other interval B[i]
            b_overlap_a = B[j][start] >= A[i][start] and B[j][start] <= A[i][end]
            
            # save the intersection part
            if (a_overlap_b or b_overlap_a):
                result.append([max(A[i][start],B[j][start]), min(A[i][end], B[j][end])])
                
            # move next from the interval whihc is finishing first
            if A[i][end] < B[j][end]:
                i += 1
            else:
                j += 1
        return result
