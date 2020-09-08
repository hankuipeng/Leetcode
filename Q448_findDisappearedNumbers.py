#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Created on Tue Sep  8 09:08:15 2020

@author: hankui

"""


#%%
test1 = [4,3,2,7,8,2,3,1]
test2 = [1,1]


#%% attempt 1
def findDisappearedNumbers(nums):
    l0 = len(nums)
    nums = list(set(nums))
    l1 = len(nums)
    
    import pdb
    pdb.set_trace()
    
    res = []
    
    ## if the length is 1
    if l1 == 1:
        for i in range(l1,l0+1):
            res.append(i+1)
    
    ## if the length is not 1
    else:
        for i in range(1, l0):
            diff = nums[i] - nums[i-1]
            if diff != 1:
                for d in range(diff-1):
                    res.append(nums[i-1]+d+1)

    return res



#%% attempt 2 
# reference: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/discuss/832784/O(n)-solution-wvideo-whiteboard-explanation
nums = test2 

res = []

for i,v in enumerate(nums):
    nums[abs(v)-1] = -abs(nums[abs(v)-1])

for i in range(len(nums)):
    if nums[i] > 0:
        res.append(i+1)


#%%
findDisappearedNumbers(test1)

