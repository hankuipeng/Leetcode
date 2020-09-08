#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 10:49:29 2020

@author: hankui
"""

#%%
nums = [12,345,2,6,7896]


#%%
def findNumbers(nums):
    count = 0
    for ind, val in enumerate(nums):
        if len(str(val))%2 == 0: 
            count += 1
    return count


#%%
findNumbers(nums)