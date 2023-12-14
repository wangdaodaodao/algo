"""
Name: algo lesson 2 
Author: wangdaodao
Date: 2023-11-20
Version: 1.0
Description: 王导导算法课程学习.
"""

import time
#递归





def recur(n):
    if n == 1:
        return 1    
    res = recur(n-1)
    return res+n


t1 = time.time()
print(recur(100))
t2 = time.time()

print(t2-t1)