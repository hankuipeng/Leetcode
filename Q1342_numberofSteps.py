#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 22:30:06 2020

@author: hankui
"""


#%%
num = 8

def numberofSteps(num):
    count = 0
    while num > 0:
        if num % 2 == 0:
            num = num/2
            count += 1
        else:
            num = num - 1
            count += 1
    return count