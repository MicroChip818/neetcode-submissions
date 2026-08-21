class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr_max = max(arr)
        for i, n in enumerate(arr):
            if n < curr_max:
                arr[i] = curr_max

            elif i < len(arr) - 1:
                curr_max = max(arr[i + 1:])
                arr[i] = curr_max

            else:
                arr[i] = -1

        return arr