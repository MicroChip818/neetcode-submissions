from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Create the sliding window and a set for seen chars
        window = deque()
        seen_window = set()
        max_length = 0
        
        # Iterate through the loop
        for c in s:
            # Check if character is already seen
            while c in seen_window:
                max_length = len(window) if len(window) > max_length else max_length
                window.popleft()
                seen_window.discard(c)
                if c not in seen_window:
                    seen_window = set(window)

            # Add characters to the sliding window and hash set
            window.append(c)
            seen_window.add(c)

        max_length = len(window) if len(window) > max_length else max_length

        # Return the length of the longest substring
        return max_length