class Solution:
    def calculate(self, s: str) -> int:
        stack, curr, sign = [], 0, 1
        i = 0
    
        while i < len(s):
            if s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                curr += sign * num
                i -= 1
            elif s[i] == '+': 
                sign = 1
            elif s[i] == '-': 
                sign = -1
            elif s[i] == '(':
                stack.append((curr, sign))
                curr, sign = 0, 1
            elif s[i] == ')':
                prev_curr, prev_sign = stack.pop()
                curr = prev_curr + prev_sign * curr
            i += 1
    
        return curr
        