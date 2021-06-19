'''you are given N scores. Store them in a list and find the score of the runner-up.'''
n=int(input())
score=list(map(int,input().split()))[:n]
score.sort(reverse=True)
for i in score:
    if i!=score[0]:
       print(i)
       break
else:print("NO runner-up")

