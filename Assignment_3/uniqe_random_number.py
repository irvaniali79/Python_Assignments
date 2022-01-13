from random import randint

n=int(input())

arr=set()
length=0
for i in range(n):
    length=len(arr)
    arr.add(randint(0,100))

    if length==len(arr):
        n+=1
print (arr)