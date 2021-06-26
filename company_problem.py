''' A Company has decided to give some gifts to all of its employees. For that, the company has
given some rank to each employee. Based on that rank, the company has made certain rules to distribute the gifts.
The rules for distributing the gifts are:
Each employee must receive at least one gift.
Employees having higher ranking get a greater number of gifts than their neighbours.
What is the minimum number of gifts required by the company?
Constraints
1 < T < 10
1 < N < 100000
1 < Rank < 10^9
Input
First line contains integer T, denoting the number of test cases.
For each test case:
First line contains integer N, denoting the number of employees.
Second line contains N space separated integers, denoting the rank of each employee.
'''
t=int(input("Number of test cases:"))
for k in range(t):

  n=int(input("Number of employees:"))

  l=list(map(int,input("N seperated integer denoting ranks of employee:").split(' ')))

  m = [int(1)]*len(l)

  for i in range(0,n-1):

     if l[i]>l[i+1] and m[i]<=m[i+1]:

        m[i]=m[i]+1

        for j in range(i,0,-1):

           if l[j-1]>l[j] and m[j-1]<=m[j]:

              m[j-1]=m[j]+1;

           else:

              break

     elif l[i]<l[i+1] and m[i+1]<=m[i]:

        m[i+1]=m[i]+1

  print("Total number of gifts required for case {}:{}".format((k+1),sum(m)))