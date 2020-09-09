#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Created on Wed Sep  9 09:43:47 2020

@author: hankui

"""


#%%
test1 = [4,3,2,7,8,2,3,1]
test2 = [2, 2]


#%%
def findDuplicates(nums):
    
    res = []
    
    #import pdb
    #pdb.set_trace()
    
    for i,v in enumerate(nums):
        absv = abs(v)
        if nums[absv-1] > 0:
            nums[absv-1] = -nums[absv-1]
        else:
           res.append(abs(v)) 
    return res


#%%
findDuplicates(test2)

