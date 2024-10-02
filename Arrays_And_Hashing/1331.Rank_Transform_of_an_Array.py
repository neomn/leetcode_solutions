class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Store the rank for each number in arr
        num_to_indices = {k: [] for k in sorted(set(arr))}

        for i, num in enumerate(arr):
            num_to_indices[num].append(i)

        rank = 1
        for num in num_to_indices.keys():
            for index in num_to_indices[num]:
                arr[index] = rank
            rank += 1

        return arr
