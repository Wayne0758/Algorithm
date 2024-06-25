#weight considered
lis1 = []
with open("cost239", "r") as file:
  for line in file:
      a=line.rstrip().split()
      b = list(int(i) for i in a)
      lis1.append(b)
nodenum=int(lis1[0][0])
A = [[0]*nodenum for _ in range(nodenum)]
ed=[]
t=0
for i in range(1,len(lis1)):
  if(A[lis1[i][0]][lis1[i][1]]==0 and A[lis1[i][0]][lis1[i][1]]==0):
    A[lis1[i][0]][lis1[i][1]]=1
    A[lis1[i][1]][lis1[i][0]]=1
    ed.append([lis1[i][0],lis1[i][1],lis1[i][2],t])
    t+=1

sum = 0
for i in range(nodenum):
  for j in range(nodenum):
    if A[i][j] != 0:
      sum += 1
edgenum = int(sum / 2)
cyclebasis = edgenum - nodenum + 1
b=0
s=0
e=nodenum
cycle=0
temp=[32760]*nodenum
check_re=[32760]*20000
check_cycle=[32760]*nodenum
order = [[-1]*nodenum for _ in range(20000)]
k=0
c=0
pre=0
no=0
adde=0
t=0
smallest=0
compare=0
m=0
n=0
i=0
j=0
a=[]
for i in range(nodenum):
  order[i][0]=i

for no in range(1,nodenum):
  adde=0
  s=0
  for k in range(e):
    s=s+b
    b=0
    pre=order[s][no-1]
    for i in range((order[s][0]+1),nodenum):
      if(A[pre][i]==1):
        for j in range(1,(no-1)):
          if(order[s][j]==i):
            j=-1
            break
        if(j!=-1):
          b+=1
          temp[b]=i
    c=0
    if(b>0):
      adde=adde+b-1
      for i in range(e+adde,s,-1):
        for j in range(no):
          order[i+b-1][j]=order[i][j]
      for i in range(s,(s+b)):
        c+=1
        order[i][no]=temp[c]
        for j in range(no):
          order[i][j]=order[s][j]
        if((no>1) and (A[order[i][no]][order[i][0]]==1)):
          for m in range(no+1):
            check_cycle[m]=order[i][m]
          compare=0
          for m in range(1,no+1):
            compare = compare * 10 + check_cycle[m]
          compare = compare * 10 + check_cycle[0]
          check_re[i] = 0
          for m in range(no,-1,-1):
            check_re[i] = check_re[i] * 10 + check_cycle[m]
          for m in range(i):
            if(check_re[m]==compare):
              m=-1
              break
          if(m!=-1):
            a.append(order[i][0:no+1])
            cycle+=1
    else:
      for i in range(s,(e+adde)):
        for j in range(no+1):
          order[i][j]=order[i+1][j]
      adde-=1
  e=e+adde

#Gaussian Elimination
ce = [[0]*(edgenum+2) for _ in range(cycle)]
mcb = [[-1]*edgenum for _ in range(cyclebasis)]
cn = []
for i in range(len(a)):
  for j in range(len(a[i])):
    for k in ed:
      if j != len(a[i])-1 and ((a[i][j]==k[0] and a[i][j+1]==k[1]) or (a[i][j]==k[1] and a[i][j+1]==k[0])):
        ce[i][k[3]]=1
        ce[i][-1]+=k[2]
        ce[i][-2]=i
      elif j == len(a[i])-1 and ((a[i][j]==k[0] and a[i][0]==k[1]) or (a[i][j]==k[1] and a[i][0]==k[0])):
        ce[i][k[3]]=1
        ce[i][-1]+=k[2]
        ce[i][-2]=i
ce.sort(key = lambda s: s[-1])
i=0
for j in range(len(ce)):
  flag=0
  if i == 0 or i == 1:
    mcb[i]=ce[j][:-2]
    cn.append(ce[j][-2])
    i+=1
  elif i < cyclebasis and i>1:
    mcb[i]=ce[j][:-2]
    for k in range(2**i):
      r=[0]*edgenum
      t=k
      for l in range(i):
        if t%2==1:
          r = list(a^b for a,b in zip(r,mcb[l]))
          t=int(t/2)
        else:
          t=int(t/2)
      if mcb[i]==r:
        flag=1
    if flag==0:
      mcb[i]=ce[j][:-2]
      cn.append(ce[j][-2])
      i+=1
  else:
    break
for i in range(len(cn)):
  for j in range(len(a[cn[i]])):
    print("{}->".format(a[cn[i]][j]),end='')
  print("{}".format(a[cn[i]][0]))
