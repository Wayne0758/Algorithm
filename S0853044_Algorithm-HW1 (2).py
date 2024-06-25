# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 15:34:29 2022

@author: wayne
"""

import sys

def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = arr[start]
    low = start + 1
    high = end

    while True:
        while low <= high and arr[high] >= pivot:
            high = high - 1

        while low <= high and arr[low] <= pivot:
            low = low + 1

        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break

    arr[start], arr[high] = arr[high], arr[start]

    p = high
    quick_sort(arr, start, p - 1)
    quick_sort(arr, p + 1, end)

def insertion_sort(arr, Len):

    if Len <= 1:
        return
    insertion_sort(arr, Len - 1)
    end = arr[Len - 1]
    
    i = Len - 2
    while(i >= 0 and arr[i] > end):
        arr[i + 1] = arr[i]
        i = i - 1

    arr[i + 1] = end
    
f = open("test1.txt", "r")
line = f.read().split()
lis1 = list(float(i) for i in line)
decision = int(input("1執行快速排序法，2執行插入排序法，3程式結束:"))
f.close()

if decision == 1:
    quick_sort(lis1, 0, len(lis1) - 1)  
elif decision == 2:
    insertion_sort(lis1, len(lis1))
elif decision == 3:
    sys.exit(0)

print("結果:", lis1) 
print("所有數的個數:", len(lis1))
print("最大的數:", max(lis1))
print("最小的數:", min(lis1))

