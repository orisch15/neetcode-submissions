class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = 0
        stack = []

        for c in tokens:
            if c == '+':
                x, y = stack.pop(), stack.pop()
                stack.append(y + x)
            elif c == '-':
                x, y = stack.pop(), stack.pop()
                stack.append(y - x)
            elif c == '*':
                x, y = stack.pop(), stack.pop()
                stack.append(y * x)
            elif c == '/':
                x, y = stack.pop(), stack.pop()
                stack.append(int(float(y) / x))
            else:
                stack.append(int(c))
        return stack[0]

        