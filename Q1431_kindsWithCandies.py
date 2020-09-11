#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Created on Fri Sep 11 10:31:51 2020

@author: hankui

"""


#%%
candies = [2,3,5,1,3]
extraCandies = 3


#%% attempt 1
def kidsWithCandies(candies, extraCandies):
    
    #res = ['false']*len(candies)
    res = ['false' for _ in range(len(candies))]
    max_val = max(candies)
    
    for i in range(len(candies)):
        if candies[i] + extraCandies >= max_val:
            res[i] = 'true'
    return res


#%% attempt 2
def kidsWithCandies(candies, extraCandies):
    output = []
    max_candy = max(candies)
    for i in candies:
        if (extraCandies+i)>=max_candy:
            output.append(True)
        else:
            output.append(False)
    return output


#%%
kidsWithCandies(candies, extraCandies)