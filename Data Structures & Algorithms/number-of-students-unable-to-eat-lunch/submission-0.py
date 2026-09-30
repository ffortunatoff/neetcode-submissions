class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sandwiches.reverse()
        queue = deque(students)
        
        while sandwiches :
            top_sandwich = sandwiches[-1]
            if top_sandwich not in queue:
                return len(queue)

            student = queue.popleft()
            if top_sandwich == student:
                sandwiches.pop()
            else:
                queue.append(student)
        
        return 0
                

