# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        for i in strs:
            key = "".join(sorted(i))
            if key in words:
                words[key].append(i)
            else:
                words[key] = [i]
        return words.values()

  #same concept but cleaner

  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)
        for i in strs:
            words["".join(sorted(i))].append(i)
        return words.values()