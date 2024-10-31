class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        lowest = nums[0]
        while (lo < hi):
            mid = (lo + hi) // 2

            lowest = min(nums[lo], lowest)
            lowest = min(nums[mid], lowest)
            lowest = min(nums[hi], lowest)
            
            if (nums[mid] < nums[lo]):
                hi = mid - 1
            else:
                lo = mid + 1

        return lowest