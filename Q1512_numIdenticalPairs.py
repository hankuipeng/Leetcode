#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Sep 15 22:03:32 2020

@author: hankui
"""

# Link to question: https://leetcode.com/problems/number-of-good-pairs/

#%%
nums = [1,2,3,1,1,3]


#%%
#import itertools
#[(g[0], len(list(g[1]))) for g in itertools.groupby(nums)]

import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)


from collections import Counter

ctr = Counter(nums)
freqs = [ctr[v] for v in ctr]

res = 0
for i in range(len(freqs)):
    if freqs[i] > 1:
        res += nCr(freqs[i], 2)


#%%
# def numIdenticalPairs(nums):