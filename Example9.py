A=[1,2,3,4,5]
B=[]
x=0
n=0
e=1
while x!=(len(A)):
    if x==0:
        B.append(A[x])
    if x%2==1:
        B.append(A[len(A)-1-n])
        n+=1
    if x%2==0 and x!=0:
        B.append(A[x-e])
        e+=1

    x+=1

print (B)
