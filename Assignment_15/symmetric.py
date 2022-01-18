import math
def Is_Symmetric(string):
    for i in range(0,math.floor(len(string)/2)):
        if string[i] == string [len(string)-(i+1)]:
            continue
        else :
            return False
    return True        

string = str(input())

if (Is_Symmetric(string)):
    print ("Yes")
else:
    print ("No")