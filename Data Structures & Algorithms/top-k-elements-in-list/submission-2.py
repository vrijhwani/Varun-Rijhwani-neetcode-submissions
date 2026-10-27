class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map1 ={}
        freq = [[]for i in range(len(nums)+1)]

        for i in nums:
            map1[i] = map1.get(i,0) + 1

        for n,c in map1.items():
            freq[c].append(n)

        res = []

        for s in range(len(freq)-1, 0,-1):
            for j in freq[s]:
                res.append(j)
                if len(res)==k:
                    return res
        return res