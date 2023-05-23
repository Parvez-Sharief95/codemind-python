l=int(input())
r=int(input())
c=0
for i in range(l,r+1):
    x=0
    for j in range(i,r+1):
        x+=j
        if x%2:
            c+=1
print(c)