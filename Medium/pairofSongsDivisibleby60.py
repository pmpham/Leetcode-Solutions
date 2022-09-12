# 1010. Pairs of Songs With Total Durations Divisible by 60
# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        time = [x%60 for x in time]
        map = {}
        for i,x in enumerate(time):
            if (60-x) % 60 in map:
                count+=map[(60-x) % 60]
            if x in map:
                map[x] += 1
            else:
                map[x] = 1
        return count
            
#another solution
def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        dic = collections.defaultdict(int)
        for i in time:
            if not i%60:
                count+= dic[0]
            else:
                count += dic[60-i%60]
            
            dic[i%60] +=1
        return count