class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        min_pos = 0
        max_pos = 0
        count = 0  # Initialize variables to keep track of the minimum and maximum reach, and the number of taps used.
        
        while max_pos < n:  # Continue looping until we cover the entire range from 0 to n.
            for i in range(len(ranges)):
                # Check if tap i can cover the current minimum position (min_pos) and reach the current maximum position (max_pos).
                if i - ranges[i] <= min_pos and i + ranges[i] >= max_pos:
                    max_pos = i + ranges[i]  # Update the maximum reach if this tap can cover the current range.
                    
            if max_pos == min_pos:
                return -1  # If max_pos is not updated in this loop, it means we can't extend the reach further. Return -1 as it's not possible.
            
            count += 1  # Increment the count of taps used.
            min_pos = max_pos  # Update the minimum reach to the newly reached maximum position.
            
        return count  # Return the count of taps used to