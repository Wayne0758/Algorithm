# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 09:31:11 2022

@author: wayne
"""

a,b=map(str,input('輸入兩個正整數:').split())
al=list("0"+a)
bl=list("0"+b)
dp=[[0]*(len(b)+1) for _ in range(len(a)+1)]
prev=[[0]*(len(b)+1) for _ in range(len(a)+1)]
lcs=[0]*min(len(a),len(b))
ans=[]
def findLCSI(i,j,k,lis1):
  if len(lis1)==k:
    ans.append(lis1[:])
    return
  if i == 0 or j == 0:
    return
  if prev[i][j] == 0:
    lis1.append(al[i])
    findLCSI(i-1, j-1,k,lis1)
    lis1.pop()
  elif prev[i][j] == 1:
    findLCSI(i, j-1,k,lis1)
  elif prev[i][j] == 2:
    findLCSI(i-1, j,k,lis1)
  elif prev[i][j] == 3:
    findLCSI(i, j-1,k,lis1)
    findLCSI(i-1, j,k,lis1)

def LCSI():
  for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
      if al[i]==bl[j]:
        dp[i][j]=dp[i-1][j-1] + 1
        prev[i][j] = 0
      else:
        if dp[i-1][j] < dp[i][j-1]:
          dp[i][j] = dp[i][j-1]
          prev[i][j] = 1
        elif dp[i-1][j] > dp[i][j-1]:
          dp[i][j] = dp[i-1][j]
          prev[i][j] = 2
        elif dp[i-1][j] == dp[i][j-1]:
          dp[i][j] = dp[i-1][j]
          prev[i][j] = 3
  for i in range(len(a),0,-1):
    for j in range(len(b),0,-1):
      if dp[i][j]==dp[-1][-1] and prev[i][j]==0:
        findLCSI(i,j,dp[-1][-1],[])
LCSI()

lis2 = []
for i in range(len(ans)):
  ans[i].reverse()
  ans[i]="".join(ans[i])
  if ans[i] not in lis2:
    lis2.append(ans[i])
for i in range(dp[-1][-1]-1,-1,-1):
  lis2.sort(key=lambda x:x[i])
c=lis2[-1]
print(c.lstrip('0'))