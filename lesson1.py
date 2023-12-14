"""
Name: algo lesson 1
Author: wangdaodao
Date: 2023-11-11
Version: 1.0
Description: 王导导算法课程学习.
"""

import time
#for循环 实现1+2+3+......+n
def loop(n):
    # n = int(input('please enter your nubner:'))
    result = 0
    for i in range(1,n+1):
        # print('第{}次运算:{}+{}={}'.format(i,result, i,result+i))
        result = result + i
        
    # print('\n你输入的求{}累积和,他们的和是{}'.format(n, result))
    return result


#while 循环实现1+2+3+......+n

def loop_while(n):
    result = 0
    i = 1   #初始化变量
    while i < n+1:
        result = result + i
        i += 1  #更新变量
    print(result)
    return result



# [1,2,3,4,5,6,7,8,9,10]

def loop_while_2(n):
    result = 0
    i = 1  #初始化变量
    while i <= n:
        print('{}+{}={}'.format(result, i, result+i))
        result = result + i
        #更新变量
        i=i*2
        # print(i)

    print(result)
    return result



def nested_for_loop(n):
    res = ''
    for i in range(1, n+1):
        for j in range(1,n):
            res += f'({i},{j}),'
    return res





def recur(n):
    if n == 1:
        return 1    
    res = recur(n-1)
    return res+n


t1 = time.time()
print(recur(100))
t2 = time.time()

print(loop(10065600))
t3 = time.time()

print(t2-t1, t3-t2)