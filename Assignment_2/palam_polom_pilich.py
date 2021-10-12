import random
from os import system

scoures=[0,0,0]
while 5 not in scoures:

    system('clear')
    print('palam polom pilich')
    print('1.scoure',scoures[0],'\n2.scoure',scoures[1],'\n3.scoure',scoures[2],'\n')

    player1=int(input('1 : ro , 2 : posht '))
    player2=random.choice([1,2])
    player3=random.choice([1,2])

    print(player1,player2,player3)

    selection=[0,0]
    arr=[player1,player2,player3]
    posmin=0

    for i in range(len(arr)):
        selection[arr[i]-1]+=1
        for j in range(len(arr)):     
            if selection[arr[posmin]-1]>selection[arr[j]-1]:
                posmin=j
    if selection[arr[posmin]-1]==1:
        scoures[posmin]+=1
print('player',scoures.index(max(scoures))+1,'win')