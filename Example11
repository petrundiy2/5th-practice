k=int(input())
n=int(input())
A=[]
z=0
for x in range (n+1):
    A.append(0)
for x in range (n+1):
    if x<k:
        A[x]=1
    if x>=k:
        for y in range(x-k,x):
            A[x]+=A[y]
print (A[n])
