class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []

        for x, y in points:
            distance = sqrt(x ** 2 + y ** 2)
            minHeap.append([distance, x, y])
        
        heapq.heapify(minHeap)

        while k > 0:
            point = heapq.heappop(minHeap)
            res.append(point[1:])
            k -= 1

        return res