#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Sep 30 12:12:54 2020

@author: hankui

"""

# Link to question: https://leetcode.com/problems/trapping-rain-water/

# Reference: https://www.youtube.com/watch?v=XqTBrQYYUcc


#%%
test = [0,1,0,2,1,0,1,3,2,1,2,1]


#%%
class Solution:
    
    def __init__(self, height):
        self.height = height 
    
    def trap(self, height):
        
        sumWater = 0
        
        # calculate the max from left to right 
        LtoR = [height[0]]
        
        for i in range(1, len(height)):
            LtoR.append(max(height[i], LtoR[-1]))
        
        # calculate the max from right to left
        RtoL_rev = [height[-1]]
        
        for i in range(1, len(height)):
            RtoL_rev.append(max(height[-(i+1)], RtoL_rev[-1]))
        
        RtoL = RtoL_rev[::-1]
        
        # calculate the amount of water stored 
        for i in range(len(height)):
            sumWater += min(RtoL[i], LtoR[i]) - height[i]
        
        return sumWater


#%%
sol = Solution(test)
sol.trap(test)

