class Solution:
    def minimumPushes(self, word: str) -> int:
        frequency_map = Counter(word)
        frequency_queue = [-freq for freq in frequency_map.values()]
        heapq.heapify(frequency_queue)
        total_pushes = 0
        index = 0
        while frequency_queue:
            total_pushes += (1 + (index // 8)) * (
                -heapq.heappop(frequency_queue)
            )
            index += 1
        return total_pushes
