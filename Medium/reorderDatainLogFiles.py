# 937. Reorder Data in Log Files
# https://leetcode.com/problems/reorder-data-in-log-files/

#first attempt
def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letLogMap ={}
        digLogs = []
        ans = []
        for i in logs:
            if i[i.index(" ")+1:].replace(" ","").isdigit():
                digLogs.append(i)
            else:
                if i[i.index(" ")+1:] in letLogMap:
                    letLogMap[i[i.index(" ")+1:]].append(i[:i.index(" ")+1])
                else:
                    letLogMap[i[i.index(" ")+1:]] = [i[:i.index(" ")+1]]
        for i in collections.OrderedDict(sorted(letLogMap.items())):
            ident = letLogMap[i]
            ident.sort()
            for j in ident:
                ans.append(j+i)
        for i in digLogs:
            ans.append(i)
        return ans

#attempt 2
def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letLogMap ={}
        digLogs = []
        ans = []
        for i in logs:
            if i[i.index(" ")+1:].replace(" ","").isdigit():
                digLogs.append(i)
            else:
                if i[i.index(" ")+1:] in letLogMap:
                    letLogMap[i[i.index(" ")+1:]].append(i[:i.index(" ")+1])
                else:
                    letLogMap[i[i.index(" ")+1:]] = [i[:i.index(" ")+1]]
        #instead of sorting the whole dict, sorted only the keys as only those matter
        for i in sorted(letLogMap.keys()):
            ident = letLogMap[i]
            ident.sort()
            for j in ident:
                ans.append(j+i)
        for i in digLogs:
            ans.append(i)
        return ans

#attempt 3
def reorderLogFiles(self, logs: List[str]) -> List[str]:
        #helper function to easily sort the elements
        def createKey(log):
            ident, key = log.split(" ", maxsplit=1)
            return(0,key,ident) if key[0].isalpha() else (1,)
        
        return sorted(logs,key = createKey)