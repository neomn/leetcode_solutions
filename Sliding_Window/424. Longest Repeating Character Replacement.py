def characterReplacement(s, k):
    hashmap = {}
    left = maxFrequency = maxLength = 0
    for i in range(len(s)):
        hashmap[s[i]] = hashmap.get(s[i], 0) + 1


print(characterReplacement("ABAB", 2), 'correct response > 4')
print(characterReplacement("AABABBACBB", 2), 'correct response > 6')
