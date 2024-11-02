class Solution:
    def isCircularSentence(self, sentence: str) -> bool:

        if ord(sentence[0]) != ord(sentence[-1]):
            return False

        sentence = sentence.split()

        for i in range(1, len(sentence)):
            if ord(sentence[i-1][-1]) != ord(sentence[i][0]):
                return False
                
        return True
