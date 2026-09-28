class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {')':'(', ']':'[', '}':'{'}

        stack = []

        for i in s:
            if i in bracket:
                if stack and bracket[i]== stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)


        return True if not stack else  False