t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a=sorted(a)
    for j in range(0,n-2):
        if a[j+1]!=a[j]+1:
            a.append(a[j]+1)
            print(a[j]+1)
            break
    if len(a)<n:
        print(n)