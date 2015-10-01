from random import *
print ('vvedite kolichestvo kuznechikov')
n=int(input())
x=0
A=[]
while x!=n:
    A.append(randint(1,5))
    x+=1

print(A)
print ('vvedite vremya t')
t=int(input())
y=1
B=[]
z=0
while y<=t:
    B.append (A[len(A)-1])
    while z!=len(A)-1:
        B.append(A[z])
        z+=1
    z=0
    for e in range(B[0]):
        B[e+1],B[e]=B[e],B[e+1]
    if B[len(B)-1]==len(B)-1:
        C=[]
        for h in range (-1,len(B)-1):
            C.append(B[h])
        B=C[:]
    A=B[:]
    B=[]
    y+=1
    if y==t:
        print (A)
