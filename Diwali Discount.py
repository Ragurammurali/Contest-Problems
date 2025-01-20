- Link: https://www.codechef.com/problems/DIWALIDISC 
- Contest: Starters 158
- Difficulty: 180

Code:
A,B=map(int,input().split())
C=A-B
if(B>A):
    print(0)
elif(B==A):
    print(0)
elif(B<A):
    print(C)
