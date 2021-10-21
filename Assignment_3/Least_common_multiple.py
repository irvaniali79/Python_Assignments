a=int(input())
b=int(input())


for i in range(max(a,b),a*b+1):
    if not(i%max(a,b)) and not(i%min(a,b)):
        print(i)
        exit()
