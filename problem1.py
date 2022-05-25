class Solution:
    def checkValidString(self, s: str) -> bool:
        self.sol(s)
        
    def validParenthesis(self, s, numStars):
        map = {')':'(', '}':'{', ']':'['}
        stack = []
        for c in s:
            if c in map:
                if stack and map[c] != stack.pop():
                    return False
                elif numStars > 0 and stack:
                    stack.pop()
                    numStars -= 1
            else:
                stack.append(c)
        return True

    def sol(self, s):
        newString = []
        numStars = 0
        for c in s:
            if c != '*':
                numStars += 1
                newString.append(c)

        newString = ''.join(newString)
        if self.validParenthesis(newString, numStars):
            return True
        else:
            return False