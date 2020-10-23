# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 19:57:21 2020

@author: denis

"""

import random


def binary_search_mod(A, x):
    
    left = 0
    right = len(A) - 1
    
    while left <= right:
        
    
        #print(right)
        middle = int((left + right)/2)
        #print(middle)
        
        #Found it
        if A[middle] == x:
            return middle
        
        
        if A[middle] >= A[left] and A[middle] <= A[right]:
            #Default List. Doing regular binary search
            if x < A[middle]:
                #Search left side
                right = middle - 1
            else:
                #Search right side
                left = middle + 1
        elif A[middle] <= A[left] and A[middle] <= A[right]:
            #Case 2
            if x > A[middle] and x <= A[right]:
                #Search Right. Its in order so we know what range it can contain
                left = middle + 1
            else:
                #Search Left. This side contains the split
                right = middle - 1
        elif A[middle] >= A[left] and A[middle] >= A[left]:
            #Case 3
            if x < A[middle] and x >= A[left]:
                #Search left. Its in order so we know what range it can contain
                right = middle - 1
            else:
                #Search right. This side contains the split
                left = middle + 1
        else:
            print("Error")
            #Should never reach here
            
    return -1
                
          
    
#Testing function
def test_old():
    #test1 = binary_search_mod([10, 1, 2, 3, 4, 5, 6, 7, 8], 6)
    #test2 = binary_search_mod([3,4,5,6,7,8,9, 10, 1,2], 10)
    test3 = binary_search_mod([24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],12)
    #print(test1)
    #print(test2)
    print(test3)
    
test_old()

def test():
    A = []
    for i in range(1,31):
        A.append(i)
    
    k = int(random.random()*len(A))
    for i in range(k):
        a = A[0]
        del A[0]
        A.append(a)
        
    print('k:', str(k) + ', shifted array:',A)
    
    for i in range(len(A)):
        index = binary_search_mod(A, A[len(A)-i-1])
        
        if index >= 0:
            print('found', A[len(A)-i-1], 'at index:', index)
        else:
            print('element', A[len(A)-i-1],'not found in array')
            
    #Testing for element not in list
    a=34
    index = binary_search_mod(A, a)
    if index >= 0:
        print('found', a, 'at index:', index)
    else:
        print('element', a,'not found in array')
        
    
test()


    
