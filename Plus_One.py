n=int(input())
a=list(map(int,input().split()))
str1=""
for i in range(n):
    str1+=str(a[i])
s=int(str1)+1
s=str(s)
for i in s:
    print(i,end=" ")