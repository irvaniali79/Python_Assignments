from random import x

words=["glace","piano","dart","laravel","unreal","apple","car"]

correctanswer=x(words)
health=7


answer=dict()

flag=True

while True:
    flag=True
    id=0
    for char in correctanswer:
        if (correctanswer.index(char,id) in answer) and (char == answer[correctanswer.index(char,id)]):
            print(char,end='')
        else:
            print("_",end='') 
            flag=False
        id+=1

    if flag==1:
        print("\n Win ")
        break

    ans=input("\nEnter a letter : ")
    pos=int(input("\nEnter a pos : "))

    if ans == correctanswer[pos]:
        answer[pos]=ans
        print("correct")
    else:
        print("fault")
        health-=1
    
    if health==0:
        print ("The answer is :" ,correctanswer)
        print("game over \n")

        break
