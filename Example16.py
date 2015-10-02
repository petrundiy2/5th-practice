n=int(input())
A=[1,0]
B=[]
if n!=0:
    print (A[:len(A)-1])
    for x in range(n):
        for y in range(len(A)):
            if y==0:
                B.append(1)
            if y>0:
                B.append(A[y-1]+A[y])
            if y==len(A):
                B.append(0)
        A=B[:]
        A.append(0)
        B=[]
        print (A[:len(A)-1])
