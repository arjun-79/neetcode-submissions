from heapq import heappush,heappop
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for i in nums:
            heappush(self.heap,-i)

    def add(self, val: int) -> int:
        heappush(self.heap,-val)
        l = []
        for i in range(self.k):
            l.append(heappop(self.heap))
        ans = -l[-1]
        for i in l:
            heappush(self.heap,i)
        return ans
