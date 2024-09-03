class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # Convert the string to a number by summing digit values
        current_number = 0
        for ch in s:
            position = ord(ch) - ord("a") + 1
            while position > 0:
                current_number += position % 10
                position //= 10

        # Apply digit sum transformations k-1 times
        for i in range(1, k):
            digit_sum = 0
            while current_number > 0:
                digit_sum += current_number % 10
                current_number //= 10
            current_number = digit_sum

        return current_number
