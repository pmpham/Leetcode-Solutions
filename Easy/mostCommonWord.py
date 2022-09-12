# 819. Most Common Word
# https://leetcode.com/problems/most-common-word/

def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        dic = defaultdict(int)
        word = ""
        for i in paragraph:
            if i.isalnum():
                word+=(i.lower())
            elif(word!="" and word not in banned):
                dic[word]+=1
                word = ""
            else:
                word = ""
        if(word!="" and word not in banned):
            dic[word]+=1
            word = ""
        else:
            word = ""
        return max(dic, key=dic.get)