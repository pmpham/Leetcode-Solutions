# 150. Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/

def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+","-","*","/"]
        i = 0
        while len(tokens)>1:
            #temp = 0
            if tokens[i] in ops:
                op = tokens[i]
                temp = 0
                if op == "+":
                    temp = int(tokens[i-2]) + int(tokens[i-1])
                elif op == "-":
                    temp = int(tokens[i-2]) - int(tokens[i-1])
                elif op == "*":
                    temp = int(tokens[i-2]) * int(tokens[i-1])
                else:
                    temp = int(tokens[i-2]) / int(tokens[i-1])
                tokens[i-2] = temp
                del tokens[i]
                del tokens[i-1]
                i = i-1
            else:
                i +=1
        return int(tokens[0])