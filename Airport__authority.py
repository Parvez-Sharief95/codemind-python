def amount(n,lst,t):
    s=0
    for i in range(n):
        if lst[i]>t:
            s+=2
        else:
            s+=1
    return s
lst=[]
n=int(input())
for i in range(n):
    w=int(input())
    lst.append(w)
t=int(input())
print(amount(n,lst,t))