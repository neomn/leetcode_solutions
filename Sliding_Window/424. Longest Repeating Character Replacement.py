def characterReplacement(s, k):
    hashmap = {}
    left = maxFrequency = maxLength = 0
    for i in range(len(s)):
        hashmap[s[i]] = hashmap.get(s[i], 0) + 1
        maxFrequency = max(maxFrequency, hashmap.get(s[i]))
        windowSize = i + 1 - left
        if windowSize - maxFrequency > k:
            hashmap[s[left]] -= 1
            left += 1
            windowSize = i + 1 - left
        maxLength = max(maxLength, windowSize)
    return maxLength


print(characterReplacement("ABAB", 2), 'correct response > 4', "\n")
print(characterReplacement("AABABBACBB", 2), 'correct response > 6', "\n")
print(characterReplacement("AAAA", 0),  'correct response > 4', "\n")
