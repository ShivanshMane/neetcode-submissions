'''
Understanding the solution = 
    Input - given an array of prereq, where prereq[i] = [a,b],first take course b, before a
    Goal - find if we can take the prereq courses, before taking the numcourse
    Ouput - return true, if possible to take prereq before numcourse, otherwise false
Constraints = what if array is empty 
            = what if numcourse is same as the prereq
            = max length of prereq array 
Examples = Input = numCourse = 2, prereq = [[0,1]], Output = true 
         = Input = numCourse = 2, prereq = [[0,1],[1,0]], Output = false
Solution = 
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqMap = {i:[] for i in range(numCourses)}

        for course,prereq in prerequisites:
            prereqMap[course].append(prereq)

        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            
            if prereqMap[course] == []:
                return True 

            visiting.add(course)

            for prereq in prereqMap[course]:
                if not dfs(prereq):
                    return False
                
            visiting.remove(course)

            prereqMap[course] = []

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True

