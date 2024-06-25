# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 13:30:03 2022

@author: wayne
"""
lis1 = []
with open("test2.txt", "r") as file:
    for line in file:
        a=line.rstrip().split()
        b = list(float(i) for i in a)
        b.append(0)
        lis1.append(b)
lis1 = lis1[:2000]
def max_heap(arr,n):
    for i in range(n):
        if arr[i][0]>arr[int((i-1)/2)][0]:
            j=i
            while arr[j][0]>arr[int((j-1)/2)][0]:
                (arr[j],arr[int((j - 1) / 2)]) = (arr[int((j - 1) / 2)],arr[j])
                j = int((j - 1) / 2)
def heap_sort(arr,n):
    for i in range(n,0,-1):
        max_heap(arr,i)
        (arr[0],arr[i-1])=(arr[i-1],arr[0])
heap_sort(lis1, len(lis1))

def ranking(arr,start,end):
    if start >= end:
        return
    else:
        a = arr[start:int((end+start)/2)+1]
        b = arr[int((end+start)/2)+1:end+1]
    ranking(arr, start, int((end+start)/2))
    ranking(arr, int((end+start)/2)+1, end)
    for i in range(len(b)):
        for j in range(len(a)):
            if b[i][1]>a[j][1]:
                b[i][2]+=1
    arr[int((end+start)/2)+1:end+1]=b
ranking(lis1,0,len(lis1)-1)
for i in range(len(lis1)):
    print(lis1[i])
lis2=[i[2] for i in lis1]
print("檔案中所有點的個數:{}".format(len(lis2)))
print("最大rank:{}".format(max(lis2)))
print("最小rank:{}".format(min(lis2)))
print("平均rank(到小數點下兩位):{}".format(round(sum(lis2)/len(lis2),2)))
