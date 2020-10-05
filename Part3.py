# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 19:57:21 2020

@author: denis

PART 3
"""

#binary search is O(logn) so I will use a version of that

def binary_search_mod(A, x):
    
    left = 0
    right = len(A) - 1
    
    while left <= right:
    
        #print(right)
        middle = int((left + right)/2)
        #print(middle)
        
        if A[middle] == x:
            return middle
        elif A[middle] < x:
            
            if x > A[right] and A[right] > middle:
                #search left
                right = middle - 1
            else:
                #search right
                left = middle +1
        elif A[middle] > x:
            
            if x < A[0] and middle > A[0]:
                #search right
                left = middle + 1
            else:
                #search left
                right = middle - 1
                
          
    
#Testing function
def test():
    test1 = binary_search_mod([10, 1, 2, 3, 4, 5, 6, 7, 8], 6)
    test2 = binary_search_mod([3,4,5,6,7,8,9, 10, 1,2], 10)
    print(test1)
    print(test2)
    
test()