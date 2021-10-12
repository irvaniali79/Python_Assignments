side_1=int(input("enter 1st number: "))
side_2=int(input("enter 2st number: "))
side_3=int(input("enter 3rd number: "))

if side_1>0 and  side_2>0  and side_3>0 and side_1<side_2+side_3 and side_2<side_1+side_3 and side_3<side_1+side_2:print("OK")
else :print("NO")

