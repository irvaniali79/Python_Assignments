
arr=[]
n=int(input())

for i in range(n):
    arr+=[int(input())]

if sorted(arr)==arr:
    print('array is sorted')
else:
    print('not sorted')