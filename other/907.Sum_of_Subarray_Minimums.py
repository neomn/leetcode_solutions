class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # E.g., [3, 1, 2, 5, 4]
        # [3]
        # [3,1] [1]
        # [3,1,2] [1,2] [2]
        # [3,1,2,5] [1,2,5] [2,5] [5]
        # [3,1,2,5,4] [1,2,5,4] [2,5,4] [5,4] [4]

        arr = [0] + arr
        stack = [0]
        ans = [0] * len(arr)

        for i in range(len(arr)):
            while arr[stack[-1]] > arr[i]:
                stack.pop()
            j = stack[-1]
            ans[i] = ans[j] + (i-j)*arr[i]
            stack.append(i)
        
        return sum(ans) % (10**9 + 7)
