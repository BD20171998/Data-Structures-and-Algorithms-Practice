'''
Word Machine

You are given a list of strings ops where each element is either:

A non-negative integer that should be pushed into a stack
"POP" meaning pop the top element in the stack
"DUP" meaning duplicate the top element in the stack
"+" meaning pop the top two and push the sum
"-" meaning pop the top two and push top - second
Return the top element in the stack after applying all operations. 
If there are any invalid operations, return -1.
'''


class Solution:
    def solve(self, ops):

        stack = []
        for op in ops:

            if op.isdigit():
                stack.append(int(op))

            elif op == 'POP':
                if len(stack) > 0:
                    stack.pop()
                else:
                    return -1

            elif op == 'DUP':
                if len(stack) > 0:
                    stack.append(stack[-1])
                else:
                    return -1

            elif op == '+':
                if len(stack) > 1:
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(x+y)
                else:
                    return -1

            elif op == '-':
                if len(stack) > 1:
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(x-y)
                else:
                    return -1

        return stack[-1]
