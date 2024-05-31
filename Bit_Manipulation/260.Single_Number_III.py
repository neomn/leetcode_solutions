class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:


        xor1 = 0
        for num in nums:
            xor1 ^= num

        rightmost_set_bit = xor1 & (-xor1)

        # Step 6: Initialize variables to store the XOR of elements in the two groups
        xor2 = 0
        xor3 = 0

        # Step 7: Partition the array into two groups and calculate the XOR
        for num in nums:
            if num & rightmost_set_bit:
                xor2 ^= num
            else:
                xor3 ^= num

        # Step 9: Return the two unique numbers
        return [xor2, xor3]
