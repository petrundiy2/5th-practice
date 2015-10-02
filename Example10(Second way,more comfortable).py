from random import *
print ('vvedite kolichestvo kuznechikov')
n=int(input())
x=0
A=[]
while x!=n:
    A.append(randint(1,n-1))
    x+=1
print(A)
print ('vvedite vremya t')
t=int(input())
for x in range (len(A)-1):
    A.insert(0,A[len(A)-1])
    A=A[:len(A)-1]
    A.insert(A[0]+1,A[0])
    A=A[1:len(A)]
print (A)
