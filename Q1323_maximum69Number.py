#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 11:16:59 2020

@author: hankui
"""


#%%
num = 9669


#%%
class Solution:
    def maximum69Number (self, num: int) -> int:
        li = list(str(num))
        for i,v in enumerate(str(num)):
            if int(v) == 6:
                li[i] = 9
        return 
                


#%%
Solution.maximum69Number(__, num)