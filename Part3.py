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
            
    return "Did not find value!"
                
          
    
#Testing function
def test():
    #test1 = binary_search_mod([10, 1, 2, 3, 4, 5, 6, 7, 8], 6)
    #test2 = binary_search_mod([3,4,5,6,7,8,9, 10, 1,2], 10)
    test3 = binary_search_mod([24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],24)
    #print(test1)
    #print(test2)
    print(test3)
    
test()


    