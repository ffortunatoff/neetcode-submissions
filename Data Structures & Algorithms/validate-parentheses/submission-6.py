class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        char_map = {'[':']', '(':')', '{':'}'}
        for char in s:
            if char in '({[':
                stack.append(char)
                print(stack)
            elif char in ']})':
                if not stack or (stack and char_map[stack.pop()] != char):
                    return False
        return True if not stack else False

            
        