
number=input()
numofdigits=len(number)
val=int(number)

for digit in number:
    sum+=int(digit)**numofdigits

if val==sum:
    print('yes')
else:
    print('no')

