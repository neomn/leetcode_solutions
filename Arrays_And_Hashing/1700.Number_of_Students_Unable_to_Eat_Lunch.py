class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stu, i = Counter(students), 0
        for s in sandwiches: 
            if stu[s] == 0: 
                break
            stu[s] -= 1
            i += 1
        return len(sandwiches)-i 
