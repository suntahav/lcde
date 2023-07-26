class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in range(len(s)):
            if len(stack) == 0:
                stack.append(s[i])
            elif (ord(stack[-1]) == ord(s[i])-1) or (ord(stack[-1]) == ord(s[i])-2):
                stack.pop()
            else:
                stack.append(s[i])
        return len(stack) == 0