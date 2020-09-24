#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Sep 21 19:09:18 2020

@author: hankui

"""

# Link to question: https://leetcode.com/problems/decompress-run-length-encoded-list/

#%% frequency and value combo
nums = [1,2,3,4]


#%%
res = []

for i in range(int(len(nums)/2)):
    # frequency: i*2
    # value: i*2 + 1
    
    list_cur = [nums[i*2+1]]*nums[i*2]
    res.extend(list_cur)
    