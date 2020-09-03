class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        
        # k-way merge
        # use max heap
        
        max_heap = []
        
        for i in range(0, min(k,len(nums1))):
            for j in range(min(k, len(nums2))):
                if len(max_heap) < k:
                    heappush(max_heap,(-nums1[i]-nums2[j],i,j))
                else:
                    if -(nums1[i] + nums2[j]) < max_heap[0][0]:
                        print(nums1[i],nums2[j])
                        break
                    else:
                        heappop(max_heap)
                        heappush(max_heap,(-nums1[i]-nums2[j],i,j))
        
        result = []
        for (num,i,j) in max_heap:
            result.append([nums1[i],nums2[j]])
        
        return result
