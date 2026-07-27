class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr_max = max(arr)
        for i, num in enumerate(arr):
            if num == curr_max:
                if arr[i+1:]:
                    curr_max = max(arr[i+1:])
                else:
                    curr_max = -1
            arr[i] = curr_max
        return arr