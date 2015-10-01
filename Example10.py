from random import *
print ('vvedite kolichestvo kuznechikov')
n=int(input())
x=0
A=[1,2,3,4,2]

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
    A=B[:]
    B=[]
    y+=1
print (A)
