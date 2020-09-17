#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Sep 16 22:45:19 2020

@author: hankui

"""

# Link to question: https://leetcode.com/problems/shuffle-string/


#%%
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]


#%%
def restoreString(s, indices):
    
    res = list(s)
    
    for i, v in enumerate(indices):
        res[v] = s[i]
        #print(res)
    return ''.join(res)
    
restoreString(s, indices)