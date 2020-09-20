#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Sep 20 15:18:38 2020

@author: hankui

"""

# Link to question: https://leetcode.com/problems/count-of-smaller-numbers-after-self/

#%%
nums = [5, 2, 6, 1]


#%% Attempt 1
# The following solution works, but exceeds the time limit 

nums_rev = nums[::-1] # the original list in reverse order 

## find the number of smaller numbers to the left of the current number
import numpy as np

index_ordered = np.argsort(nums_rev)

smaller = [i for i in range(len(nums_rev))]


res = []
result = [0 for _ in range(len(nums))]

for i,v in enumerate(index_ordered):
    
# =============================================================================
#     import pdb
#     pdb.set_trace()
# =============================================================================
    
    count = 0
    
    for c in range(v):
        if nums_rev[v] > nums_rev[c]:
            count += 1
            
    res.append(count)
    

for i, v in enumerate(index_ordered):
    result[v] = res[i]

