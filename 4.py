class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if (len(nums1) > len(nums2)):
            tmp = nums2
            nums2 = nums1
            nums1 = tmp
        
        # len(nums1) <= len(nums2) now
        lo = 0
        hi = len(nums1) - 1
        while True:
            mid = (lo + hi) // 2
            mid2 = ((len(nums1) + len(nums2)) // 2) - mid - 2
            
            # 4 partitions: nums1_p1, nums1_p2, etc.
            nums1_p1_last = nums1[mid] if (mid >= 0) else -99999999
            nums2_p1_last = nums2[mid2] if (mid2 >= 0) else -99999999

            nums1_p2_first = nums1[mid + 1] if (mid + 1 < len(nums1)) else 99999999
            nums2_p2_first = nums2[mid2 + 1] if (mid2 + 1 < len(nums2)) else 99999999

            if (nums1_p2_first >= nums2_p1_last and nums2_p2_first >= nums1_p1_last):
                if ((len(nums1) + len(nums2)) % 2 == 0):
                    num1 = max(nums1_p1_last, nums2_p1_last)
                    num2 = min(nums1_p2_first, nums2_p2_first)
                    return ((num1 + num2) / 2)
                else:
                    return min(nums1_p2_first, nums2_p2_first)
            elif (nums1_p2_first < nums2_p1_last):
                lo = mid + 1
            else:
                hi = mid - 1