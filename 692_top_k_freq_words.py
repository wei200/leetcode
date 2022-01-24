class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        
        # use intuition, dictionary
        # Time: count the frequency in O(N), sort in O(NlogN)
        # Space: 
        # count = collections.Counter(words)
        # ans = count.keys()
        # # negative means descending, since default is ascending. w means order the words alphabetically if           # counts are equal
        # ans.sort(key = lambda w: (-count[w], w))
        # return ans[:k]
        
        
        # heap
        # turn the count dictionary into a heap, then pop the top k
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in xrange(k)]
