import math

print('1.cos\n2.sin\n3.tan\n4.cot\n5.log\n')
selection = int(input("select your oprator:[enter oprator number]: "))
number = float(input("enter number: "))


if selection==1:
    print('cos',number,'=',math.cos(math.radians(number)))
elif selection==2:
    print('sin',number,'=',math.sin(math.radians(number)))
elif selection==3:
    print('tan',number,'=',math.tan(math.radians(number)))
elif selection==4:
    print('cot',number,'=',1/math.tan(math.radians(number)))
elif selection==5:
    print('log',number,'=',math.log(number))
