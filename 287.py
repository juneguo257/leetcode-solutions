class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # every nums[x] call is a step forward on x
        slow = nums[nums[0]]
        fast = nums[nums[nums[0]]]
        while (slow != fast):
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow2 = nums[0]
        while (slow != slow2):
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow