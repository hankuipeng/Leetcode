#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Oct  4 12:25:57 2020

@author: hankui

"""

# Link to question: https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

#%%
test = [2,1,2,5,3,2]


#%%
from collections import Counter
ctr = Counter(test)

for v in ctr:
    if ctr[v] != 1:
        ans = v

[ctr[v] for v in ctr]