#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Thu Sep 17 12:29:13 2020

@author: hankui

"""

# Link to question: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

#%% test case 
nums = [8,1,2,2,3]


#%%
import numpy as np

list_ordered = sorted(list(nums))

list_set_ordered = sorted(list(set(nums)))

from collections import Counter

ctr = Counter(list_ordered)
freqs = [ctr[v] for v in ctr]


smaller_cnt = []
for i in range(len(list_set_ordered)):
    smaller_cnt.extend([sum(freqs[:i])]*ctr[list_set_ordered[i]])

ind_li = np.argsort(list(nums))

res = [0 for _ in range(len(nums))]

for i, v in enumerate(ind_li):
    res[v] = smaller_cnt[i]


#%% 
# What the question is really asking is to return the index of a sorted list.
import numpy as np
nums = np.array(nums)

res = nums
i = 0



res[i] = nums[ind_li[0]]



#%%
from collections import Counter

ctr = Counter(nums)
ctr


sorted_li = sorted(list(set(nums)))
sorted_li

ind_li = np.argsort(list(set(nums)))

ctr[sorted_li[0]]

freqs = []
freq = 0
for val in sorted_li:
    freq += ctr[val]
    freqs.append(freq - ctr[val])

freqs


# =============================================================================
# res = []
# for num in nums:
#     
#    cnt + ctr[num] - 1
# =============================================================================



#%% other people's solutions
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/discuss/819148/Python-3-greater-88.46-faster.-56ms-time.-Explanation-added
