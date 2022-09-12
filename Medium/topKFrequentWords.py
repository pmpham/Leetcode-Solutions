# 692. Top K Frequent Words
# https://leetcode.com/problems/top-k-frequent-words/

#more efficient i believe
def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if not words:
            return []
        
        counter = collections.Counter(words)
        
        heap = [(-c,x) for x,c in counter.items()]
        heap.sort()
        
        return([x[1] for x in heap[:k]])

#leetcode solution requires use of libraries so....
def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
            
        counter = collections.Counter(words)
        return nsmallest(k, counter.keys(), key=lambda x: (-counter[x], x))