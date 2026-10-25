class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        oper_set = ('+', '-', '*', "/")

        for token in tokens:
            if token not in oper_set:
                stack.append(token)
            else:
                operand_2 = int(stack.pop())
                operand_1 = int(stack.pop())
                if token == '+':
                    stack.append(operand_1 + operand_2)
                elif token == '-':
                    stack.append(operand_1 - operand_2)
                elif token == '*':
                    stack.append(operand_1 * operand_2)
                else:
                    stack.append(int(operand_1 / operand_2))

        return int(stack.pop())