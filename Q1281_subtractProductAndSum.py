#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 10:59:11 2020

@author: hankui
"""


#%%
n = 234


#%%
def subtractProductAndSum(n):
    li = [int(v) for v in list(str(n))]
    prods = 1
    sums = 0
    for ind, val in enumerate(li):
        prods *= val
        sums += val
    return prods-sums


#%%
subtractProductAndSum(n)