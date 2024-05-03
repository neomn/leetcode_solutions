class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1, version2 = version1.split('.'), version2.split('.')
        len1, len2 = len(version1), len(version2)
        for i in range(len1 if len1>=len2 else len2):
            n1, n2 = None, None
            if i < len1: n1 = int(version1[i])
            if i < len2: n2 = int(version2[i])
            if n1 != None and n2 != None and n1 > n2 : return 1
            if n1 != None and n2 != None and n1 < n2:  return -1 
            if n1 == None or n2 == None:
                num = n1 if n1 != None else n2
                if num == 0 : 
                    continue
                else: 
                    return 1 if n1 != None else -1
        return 0
