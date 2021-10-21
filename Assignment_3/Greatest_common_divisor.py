a=int(input())
b=int(input())


for i in range(2,min(a,b)/2 + 1):
    if not(a%i) and not(b%i) :
        print(i)
        exit()
print('1')