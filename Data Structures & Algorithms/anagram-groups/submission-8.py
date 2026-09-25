class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_map = defaultdict(list) #key:[1e,1a,1t] value:["ate","tea","eat"]

        for s in strs:
            count = [0]*26
            for char in s:
                count[ord(char) - ord("a")] += 1
            res_map[tuple(count)].append(s)
        return list(res_map.values())