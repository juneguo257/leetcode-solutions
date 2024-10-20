class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ret = []
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue

            p2 = i+1
            p3 = len(nums)-1
            while (p2 < p3):
                if (nums[i] + nums[p2] + nums[p3] == 0):
                    ret.append([nums[i], nums[p2], nums[p3]])

                    cur_p3 = p3
                    while (nums[cur_p3] == nums[p3] and (p3 > p2)):
                        p3 -= 1
                    p2 += 1
                elif (nums[i] + nums[p2] + nums[p3] > 0):
                    p3 -= 1
                else:
                    p2 += 1

        return ret