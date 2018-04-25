# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 10:34:26 2018
@author: souravg
To Do: 1>Implement myreduce function similar to reduce() in order to find the lowest element from a list of numbers.
       2>Implement myfilter function similar to filter() in order to find the prime numbers from a list of numbers.
"""
'''Passing the list of numbers, first and second element to the fiunction, compare first and second to find the lower one 
and then comparing the lowest number iteratitively with the next element in the loop to find the lowset number'''
def myreduce(list,first,second):
    if(first<=second):
        minimum = first
    else:
        minimum = second
    for i in list[2:]:
        if(i<=minimum):
            minimum = i
    return minimum       
list=[8,6,2,25,4,10,14,7,18]
print(myreduce(list,list[0],list[1]))

'''Initializing 1 as prime number by definition and then iteratitively checking if the number is divisible by any of the number lower than that number to find the list of prime numbers'''
def myfilter(list):
    prime_list=[1]
    for i in list:
        prime = 0
        for j in range(2,i):
            if(i%j == 0):
                prime = 0
                break
            else:
                prime = 1
                continue
        if(prime):
            prime_list.append(i)
    return prime_list       
list = range(1,51)
print(myfilter(list))