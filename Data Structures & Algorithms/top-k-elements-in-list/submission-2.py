import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1

        freq_heap = [(freq, num) for num, freq in frequencies.items()]
        heapq.heapify(freq_heap)
        top_nums = []

        for unique_num in freq_heap:
            heapq.heappush(top_nums, (unique_num[0], unique_num[1]))
            if len(top_nums) > k:
                heapq.heappop(top_nums)

        return [num[1] for num in top_nums]