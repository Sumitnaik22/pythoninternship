'''Rotate a given String in the specified direction by specified magnitude.
After each rotation make a note of the first character of the rotated String,
After all rotation are performed the accumulated first character as noted previously will form another string,
say FIRSTCHARSTRING. Check If FIRSTCHARSTRING is an Anagram of any substring of the Original string.
If yes print "YES" otherwise "NO". Input The first line contains the original string s.
The second line contains a single integer q. The i'th of the next q lines contains character d[i]
denoting direction and integer r[i] denoting the magnitude.'''
s = input()
n = int(input())
b = []
c = ''

for i in range(0,len(s)):
    for j in range(len(s),0,-1):
        b.append(s[i:j])

for i in range(b.count('')):
    b.remove('')

for i in range(n):
    d, t = input().split()
    t = int(t)
    if d == 'L':
        c = c + s[t]
    if d == 'R':
        c = c + s[-t]

if c in b:
    print("Yes")
else:
    print("No")
