def happy(num):
    
    seen=set()
    while num!=0 and num not in seen:
        seen.add(num)
        rem = 0
        while(num!=0):
            dig = num%10
            rem +=dig*dig
            num //=10
        num = rem
    return num == 1
    
num = int(input())

if happy(num):
    print(True)
    
else: print(False)