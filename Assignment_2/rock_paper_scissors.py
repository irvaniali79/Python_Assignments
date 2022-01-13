from  os import system 
import random

player_scoure_1=0
player_scoure_2=0


value_map ={ 
    1:"paper",
    2:"scissors",
    3:"rock"
}

while player_scoure_1<5 and player_scoure_2<5:
    system('clear')
    print('1.scoure',player_scoure_1,'\n2.scoure',player_scoure_2,'\n')
    print('1.paper\n2.scissors\n3.rock\n')

    player1=int(input("select your oprator:[enter oprator number]: "))
    player2=random.x([1,2,3])

    print("player1:",value_map[player1])
    print("player2:",value_map[player2])

    if player1 > player2 and player1!=3 :
        player_scoure_1+=1
    elif player1==player2 :
        pass
    else : 
        player_scoure_2+=1

print('player','1' if player_scoure_1>player_scoure_2 else '2','win')