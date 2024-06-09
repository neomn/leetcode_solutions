class Solution:
    def findMaxLength(self, nums):
        max_length, count, map = 0, 0, {0:-1}
        for i, num in enumerate(nums):
            count+=1 if num==1 else -1
            if count in map:
                max_length = max(max_length, i- map[count])
            else:
                map[count]=i
        return max_length    
