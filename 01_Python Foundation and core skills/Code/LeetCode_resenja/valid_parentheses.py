class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
                ")": "(",
                "]" : "[",
                "}" : "{" 
                }
        for char in s:
            if char in closeToOpen: # Da li je char jedan od kljuceva u recniku?
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return False if stack else True 
        
closeToOpen = {
                ")": "(",
                "]" : "[",
                "}" : "{" 
                }

solution = Solution()
s = "{}()["
print(solution.isValid(s))
