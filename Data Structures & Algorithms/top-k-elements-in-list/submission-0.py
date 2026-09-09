class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map1 = {}
        feq = [[] for i in range(len(nums)+1)]

        for n in nums:
            map1[n] = 1+map1.get(n,0)

        for n,c in map1.items():
            feq[c].append(n)

        res = []

        for i in range(len(feq)-1, 0, -1):
            for num in feq[i]:
                res.append(num)
                if len(res) == k:
                    return res
            

        
        

        