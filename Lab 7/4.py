import numpy as np

def printPairs(arr,n):
    n_find = False
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == n:
                print(arr[i],",",arr[j])
                n_find = True
                break
    if not n_find:
        print("No pair found")

#arr1 = np.array([7,8,10,5,3,4,2])
#printPairs(arr1,15)

arr2 = np.array([2,-3,1,9,4,5])
printPairs(arr2,6)

#arr3 = np.array([5,9,7,6,10])
#printPairs(arr3,18)