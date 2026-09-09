#class Solution:
 #   def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
#        map1 =defaultdict(list)
#        for c in strs:
#            my_list = [0]*26
#            for char in c:
#                my_list[ord(char)-ord("a")] = +1
#            map1[tuple(my_list)].append(c)
#        return list(map1.values())

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())        