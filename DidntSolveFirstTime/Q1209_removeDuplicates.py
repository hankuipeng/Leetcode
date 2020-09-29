#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Sep 29 10:30:30 2020

@author: hankui

"""

# Link to question: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

#%%
s = "deeedbbcccbdaa"
k = 3


#%%
s_li = list(s)
for i in range(len(s_li)-k+1):
    
# =============================================================================
#     import pdb
#     pdb.set_trace()
# =============================================================================
    
    seg = s_li[i:(i+k)] # segment with length k
    
    if len(set(seg)) == 1 and len(seg) == k:
        del s_li[i:(i+k)]


#%%
def removeDuplicates(self, s, k):
    for i, c in enumerate(s):
        if i < len(s) - k + 1 and s[i:i + k].count(c) == k: return self.removeDuplicates(s[:i] + s[i + k:], k)
    return s


removeDuplicates(s, k)


#%% sample solution 
# References:
# https://careerkarma.com/blog/python-missing-required-positional-argument-self/#:~:text=Conclusion-,The%20%E2%80%9Cmissing%201%20required%20positional%20argument%3A%20'self'%E2%80%9D,before%20calling%20a%20class%20method.&text=To%20solve%20this%20error%2C%20make,any%20of%20that%20class'%20methods.
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/discuss/830827/python-stack

from collections import deque
class Solution:

    def __init__(self,s,k):
        self.s=s
        self.k=k
        
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = deque([['dummy', 0]])
        
# =============================================================================
#         import pdb
#         pdb.set_trace()
# =============================================================================
        
        for ss in s:
            if stack[-1][0] == ss:
                if stack[-1][1] == k - 1:
                    stack.pop()
                else:
                    stack[-1][1] += 1
            else:
                stack.append([ss, 1])
        return ''.join([ss[0] * ss[1] for ss in stack])

sol = Solution(s, k)
sol.removeDuplicates(s, k)

