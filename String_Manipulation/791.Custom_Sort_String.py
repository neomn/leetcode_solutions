class Solution:
    def customSortString(self, order: str, s: str) -> str:
        map = {ch: ''  for ch in order}
        map['other'] = ''
        for ch in s:
            if ch in map:   map[ch] += ch
            else        :   map['other'] += ch
        return ''.join([map[ch] for ch in order]) + map['other']
