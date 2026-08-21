class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr_max = max(arr)
        for i, n in enumerate(arr):
            if i == len(arr) - 1:
                arr[i] = -1
                return arr

            if n >= curr_max:
                curr_max = max(arr[i + 1:])

            arr[i] = curr_max