'''Python program to remove Nth occurrence of the given word. Given a list of words in Python,
the task is to remove the Nth occurrence of the given word in that list.'''
s=list(input().split())
word,N=input().split()
count=0
for x in range(0,len(s)):
    if s[x]==word:
        count+=1
    if count==int(N):
        del(s[x])
        break
print(*s)
