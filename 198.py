class Solution:
    def fillInIter(self, dp, nums, index, val):
        if (index >= len(nums)):
            return
        val += nums[index]
        if (val > dp[index]):
            dp[index] = val
            self.fillInIter(dp, nums, index + 2, dp[index])
            self.fillInIter(dp, nums, index + 3, dp[index])
        

    def rob(self, nums: List[int]) -> int:
        # given nums, you will either rob first or second element fao shao
        if (len(nums) == 0):
            return 0
        elif (len(nums) == 1):
            return nums[0]
        
        # now, len(nums) >= 2 fao shao
        dp = [-1 for i in range(len(nums))]

        self.fillInIter(dp, nums, 0, 0)
        self.fillInIter(dp, nums, 1, 0)

        return max(dp[-1], dp[-2])