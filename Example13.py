A=[]
B=[]
s=0
n=0
for x in range(10):
    A.append(int(input()))
for x in range(10):
    if A[x]!=2:
        B.append(A[x])
        n+=1
    if A[x]==2 and x!=len(A)-1 and A[x+1]<=2:
        B.append(A[x])
        n+=1
    if A[x]==2 and x==len(A)-1:
        B.append(A[x])
        n+=1
for x in range (len(B)):
    s+=B[x]
print(s)
s=s//n
print (B)
print (s)
