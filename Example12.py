n=int(input())
A=[]
B=[]
s=''
k1=0
k2=0
if n%2==1:
    for x in range(n):
        A.append(int(input()))
    B=A[:]
    for x in range(n):
        for y in range(n):
            if A[x]<B[y]:
                k1+=1
            if A[x]>B[y]:
                k2+=1
        if k1==k2:
            print (A[x])
        k1=0
        k2=0
