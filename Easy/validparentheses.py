# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

def isValid(self, s: str) -> bool:
        map = {}
        map["("]= ")"
        map["["]= "]"
        map["{"]= "}"
        array = []
        if len(s)%2 == 0:
            for i in s:
                if i in map:
                    array.append(i)
                else:
                    if not array:
                        return False
                    elif i != map[array.pop()]:
                        return False
            if not array:
                return True
        return False