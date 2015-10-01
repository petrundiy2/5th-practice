n=int(input())
A=[]
B=[]
k=0
for x in range (n):
    A.append(int(input()))
    B.append(int(input()))
t=int(input())
for x in range (n):
    if A[x]<=t>=B[x]:
        k+=1
print(k)
