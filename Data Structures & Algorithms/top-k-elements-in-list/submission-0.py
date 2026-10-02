from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        heap = []
        res = []
        for key,value in freq_map.items():
            heapq.heappush(heap, (-value,key))
        for _ in range(k):
            res.append(heapq.heappop(heap)[-1])
        return res