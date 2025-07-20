class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)

        res = n
        for sandwich in sandwiches:
            count = 0
            while count < n and sandwich != students[0]:
                students.append(students[0])
                students.pop(0)
                count += 1
            
            print(students[0], sandwich)
            if sandwich == students[0]:
                res -= 1
                students.pop(0)
            else:
                break

        return res

            
                
                
        