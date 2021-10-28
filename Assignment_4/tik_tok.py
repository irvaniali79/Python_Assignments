from colorama import Fore
from random import randint
def reset():
    global game 
    game= [['-','-','-'],['-','-','-'],['-','-','-']]
    show()

def show():
    for i in range(3):
        for j in range(3):
            print(game[i][j],end='')
        print()

def gamechecker():
    if(thripel()):
        return 1
    elif gameisfull():
        return -1
    return 0

def gameisfull():
    if '-' not in game[0] and  '-'  not in game[1] and  '-'  not in game[2]:
        return True
    return False

def thripel():
    for i in range(3):
        if game[i][0]==game[i][1]==game[i][2]!='-':
            return True
        elif game[0][i]==game[1][i]==game[2][i]!='-':
            return True
        if game[0][0]==game[1][1]==game[2][2]!='-':
            return True
        elif game[0][2]==game[1][1]==game[2][0]!='-':
            return True 
    return False

def pvp():
    reset() 
    while True:

        choice('X',"one")
        show()
        if(gamechecker()==1):
            return "player 1 win"
        elif gamechecker()==-1:
            return "draw"
        choice('O',"two")
        show()
        if(gamechecker()==1):
            return "player 2 win"
        elif gamechecker()==-1:
            return "draw"

def pve():
    reset() 
    while True:

        choice('X',"one")
        show()
        if(gamechecker()==1):
            return "player 1 win"
        elif gamechecker()==-1:
            return "draw"
        choice('O',"computer")
        show()
        if(gamechecker()==1):
            return "computer win"
        elif gamechecker()==-1:
            return "draw"

def choice(char,user):
    row,col=entry(user)
    game[row][col]=char

def entry(str):
    while True:
        if(str!="computer"):
            row=int(input("enter row player "+str+" "))-1
            col=int(input("enter col player "+str+" "))-1
        else :
            row=randint(0,2)
            col=randint(0,2)
        if 0<=row<=2 and 0<=col<=2 and game[row][col]=='-':
            return row,col
        print('entry isn\'t valid')

def main():
    while True:

        print("[1]pve")
        print("[2]pvp")
        print("[3]exit")

        x=int(input())

        
        print(pvp()) if x==1 else print(pve()) if x==2 else exit(0)


if __name__=="__main__":
    global game
    game =[['-','-','-'],['-','-','-'],['-','-','-']]
    main()
print(__name__)