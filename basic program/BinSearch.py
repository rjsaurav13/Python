# -*- coding: utf-8 -*-
"""


@author: saurav
"""

def binarySearch(arr,beg,end,item):  
    if end >= beg:  
        mid = int((beg+end)/2)  
        if arr[mid] == item :  
            return mid+1  
        elif arr[mid] < item :   
            return binarySearch(arr,mid+1,end,item)  
        else:   
            return binarySearch(arr,beg,mid-1,item)  
    return -1  
      
  
arr=[1,2,3,4,90,6,7,8,9,10];  
item = int(input())  
location = -1;   
location = binarySearch(arr,0,9,item);  
if location != -1:   
    print(location)  
else:   
    print("number is not there")  