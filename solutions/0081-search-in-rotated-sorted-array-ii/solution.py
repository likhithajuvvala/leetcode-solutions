class Solution:
    def search(self, arr: List[int], k: int) -> bool:
        n = len(arr)  # size of the array
        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2

            # if mid points to the target
            if arr[mid] == k:
                return True

            # Edge case:
            if arr[low] == arr[mid] and arr[mid] == arr[high]:
                low += 1
                high -= 1
                continue

            # if left part is sorted
            if arr[low] <= arr[mid]:
                if arr[low] <= k <= arr[mid]:
                    # element exists
                    high = mid - 1
                else:
                    # element does not exist
                    low = mid + 1
            else:  # if right part is sorted
                if arr[mid] <= k <= arr[high]:
                    # element exists
                    low = mid + 1
                else:
                    # element does not exist
                    high = mid - 1

        return False


        