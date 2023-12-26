import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # print(tokens)
        arr = list()
        valid = set(['+','-','*','/'])
        for op in tokens:
            if op not in valid:
                arr.append(int(op))
            else:
                first = arr.pop()
                second = arr.pop()
                # print(first, second, arr)
                if op == '+':
                    arr.append(first+second)
                elif op == '-':
                    arr.append(second-first)
                elif op == '*':
                    arr.append(first*second)
                else:
                    res = second/first
                    if int(res)==res:
                        arr.append(int(res))
                    elif res >= 0:
                        arr.append(math.floor(res))
                    else:
                        arr.append(math.floor(res)+1)
                    # arr.append(second//first)
        return arr.pop()

        