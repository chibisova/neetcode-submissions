class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) < 2:
            return int(tokens[0])
        integers = [int(tokens[0]), int(tokens[1])]
        for c in range(2,len(tokens)):
            if tokens[c] == "+":
                res = integers[-2] + integers[-1]
                integers.pop()
                integers.pop()
                integers.append(res)
            elif tokens[c] == "-":
                res = integers[-2] - integers[-1]
                integers.pop()
                integers.pop()
                integers.append(res)
            elif tokens[c] == "/":
                res = int(integers[-2] / integers[-1])
                integers.pop()
                integers.pop()
                integers.append(res)
            elif tokens[c] == "*":
                res = integers[-1] * integers[-2]
                integers.pop()
                integers.pop()
                integers.append(res)
            else:
                integers.append(int(tokens[c]))
        return integers[0]
            

                