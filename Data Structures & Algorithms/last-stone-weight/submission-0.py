class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            res = heapq.heappop(max_heap) - heapq.heappop(max_heap)
            if res != 0:
                heapq.heappush(max_heap, res)

        return -max_heap[0] if max_heap else 0