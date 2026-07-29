import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1
        
        freq_groups = [[] for i in range(len(nums) + 1)]
        for num, freq in frequencies.items():
            freq_groups[freq].append(num)

        top_nums = []
        for i in range(len(freq_groups) - 1, -1, -1):
            curr_group = freq_groups[i]
            for num in curr_group:
                top_nums.append(num)
                if len(top_nums) == k:
                    return top_nums