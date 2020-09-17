#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Created on Sat Sep 12 10:23:55 2020

@author: hankui

"""


# Link to question: https://leetcode.com/problems/shuffle-the-array/


#%%
test = [2,5,1,3,4,7]


#%%
def shuffle(nums):
        
    half_l = int(len(nums)/2)
    
    res = []
    
    for i in range(half_l):
        #print(i)
        res.extend([nums[i],nums[i+half_l]])
        
    return res


#%%
shuffle(test)