import random

winCount = 0

for i in range(101):
    doors = [1,2,3]
    pAvailableDoors = [1,2,3] #what player sees as available doors
    hAvailableDoors = [1,2,3] #what host sees as available doors

    winningDoor = random.choice(doors) #winning door decided before game
    playerDoor = random.choice(doors) #player picks a door
    pAvailableDoors.remove(playerDoor) #playerDoor cannot be chosen again by player
    hAvailableDoors.remove(playerDoor) #playerDoor cannot be chosen again by host

    #host always picks a losing door
    if playerDoor == winningDoor:
        hostDoor = random.choice(hAvailableDoors) #there should be 2 doors available
        pAvailableDoors.remove(hostDoor) #there should be 1 unopened door visible to player
        hAvailableDoors.remove(hostDoor) #there should be 1 unopened door visible to host
    else:
        hAvailableDoors.remove(winningDoor) #winningDoor cannot be chosen by host
        hostDoor = random.choice(hAvailableDoors)
        pAvailableDoors.remove(hostDoor) #there should be 1 unopened door visible to player
        # print(pAvailableDoors)

    #doors are now arranged, host gives choice to switch
    # playerChoice = random.randrange(2)
    playerChoice = 1 #fixed setting
    #0 = stay, 1 = switch
    if playerChoice == 1:
        # print('p/s/w/h = ', playerDoor,pAvailableDoors[0],winningDoor,hostDoor)
        # print('player switched from ', playerDoor, ' to ', pAvailableDoors[0])
        playerDoor = pAvailableDoors[0]
    # else:
        # print('p/s/w/h = ', playerDoor,'s',winningDoor,hostDoor)
        # print('player stayed')
    
    if hostDoor == playerDoor or hostDoor == winningDoor:
        print('ERROR: hostDoor = ', hostDoor, ' playerDoor = ', playerDoor,' winningDoor = ', winningDoor)
        break

    #checking if the player won
    if playerDoor == winningDoor:
        if playerChoice == 1:
            # print('Player won by switching to ', playerDoor, ' which was the winning door ', winningDoor)
            winCount += 1
        else:
            # print('Player won by staying on ', playerDoor, ' which was the winning door ', winningDoor)
            winCount += 1
    # else:
    #     if playerChoice == 1:
    #         print('Player lost by switching to ', playerDoor, ' when the winning door was ', winningDoor)
    #     else:
    #         print('Player lost by staying on ', playerDoor, ' when the winning door was ', winningDoor)
        
    i += 1

print(winCount, ' won of ', i, ' games played')

i = 0
