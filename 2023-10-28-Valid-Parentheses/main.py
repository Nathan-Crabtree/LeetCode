'''
https://leetcode.com/problems/valid-parentheses/
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(0, s.__len__()):
            stack.append(s[i])
            if(i == 0):
                continue
            if(s[i] == ')'):
                if(s[i-1] == '('):
                    stack.pop()
                    stack.pop()
            if(s[i] == '}'):
                if(s[i-1] == '{'):
                    stack.pop()
                    stack.pop()
            if(s[i] == ']'):
                if(s[i - 1] == '['):
                    stack.pop()
                    stack.pop()
            #print(stack)
        if(stack.__len__() == 0):
            return True
        else:
            return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid("()"))
    print(solution.isValid("()[]{}"))
    print(solution.isValid("(]"))
    print(solution.isValid("(])["))
    print(solution.isValid("{(})"))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
