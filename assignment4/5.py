'''What is the maximum number of rava idlis that she can have?
At the idli shop there are two types of Rava Idli's available.
One goes for Rs.A per piece and the other goes for Rs.B per piece.
The girl has a total of K rupees.
Print the maximum number of idlis she can buy for each test case on a new line
first line is for no. of test cases and next line to get value of A,B,K in a single line
'''
n=int(input("Enter no.of test cases:"))
for x in range(n):
    A,B,K=list(map(int,input().split()))
    print(max(K//A,K//B))