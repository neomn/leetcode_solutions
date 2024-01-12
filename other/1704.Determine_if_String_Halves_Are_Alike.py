class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        lens = len(s)
        l, r = 0, lens//2
        vina, vinb = 0, 0
        for _ in range(lens//2):
            if s[l] in vowels:
                vina += 1
            if s[r] in vowels:
                vinb += 1
            l, r = l+1, r+1
        return vina == vinb
