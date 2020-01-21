class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        #cand_ind = [i for i in range(len(nums)) if nums[i]<=target]
        
        from itertools import combinations 
        comb = combinations(list(range(len(nums))), 2)
        for com in comb:
            if nums[com[0]] + nums[com[1]] == target: 
               res = com
               break
        return res


maps = {}
        for i in range(len(nums)):
            if (target-nums[i]) not in maps:
                maps[nums[i]] = i
            else:
                return [maps[target-nums[i]],i]
