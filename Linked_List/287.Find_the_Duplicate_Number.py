class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0,0
        while (True):
            slow, fast = nums[slow], nums[nums[fast]]
            print(slow, fast)
            if slow == fast:
                break
        slow2 = 0
        while(True):
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow2
