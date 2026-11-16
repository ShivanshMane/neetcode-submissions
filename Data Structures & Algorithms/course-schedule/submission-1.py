
'''
Understanding the Problem:
- Input: We are given an integer numCourses and a list of prerequisites.
- Each prerequisite pair [a, b] means we must complete course b before taking course a.
- Goal: Determine whether we can complete all courses without violating the prerequisite requirements.
- Output: Return True if we can finish all courses; otherwise, return False.
- The main thing we need to check is whether the prerequisite relationships contain a cycle.

Constraints:
- numCourses can be between 1 and 2000.
- The prerequisites list can be empty.
- A course cannot be its own prerequisite.
- There can be multiple prerequisites for one course.
- All course numbers are between 0 and numCourses - 1.
- Prerequisite pairs are unique.
- A cycle in the prerequisite relationships makes it impossible to finish all courses.

Examples:
1. Input:
   numCourses = 2
   prerequisites = [[0,1]]
   Output: True
   Explanation: We can take course 1 first, followed by course 0.

2. Input:
   numCourses = 2
   prerequisites = [[0,1],[1,0]]
   Output: False
   Explanation: Course 0 requires course 1, and course 1 requires course 0.
   This creates a cycle, so neither course can be completed first.

3. Input:
   numCourses = 3
   prerequisites = []
   Output: True
   Explanation: There are no prerequisites, so we can take all courses.

Approach – DFS + Cycle Detection:
1. Create a prerequisite map (adjacency list) where each course maps to a list of its prerequisites.
2. Create a visiting set to keep track of the courses currently being explored in the DFS path.
3. Define a DFS helper function that takes the current course as input.
4. Check the base cases:
   - If the course is already in the visiting set, we have found a cycle, so return False.
   - If the course has no remaining prerequisites, return True.
5. Add the current course to the visiting set to mark it as currently being explored.
6. Iterate through all prerequisites of the current course:
   - Recursively call DFS for each prerequisite.
   - If any DFS call returns False, return False because a cycle exists.
7. After exploring all prerequisites:
   - Remove the current course from the visiting set.
   - Set its prerequisite list to an empty list because we have successfully verified that course.
   - Return True.
8. Run DFS for every course to make sure all courses can be completed.
9. If any DFS call returns False, return False. Otherwise, return True.
Time and space complexity - O(V + E), v being the num of courses and e being the num of prereq
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

