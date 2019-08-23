import random
# jail is 10
# go is 0
#
def monopoly_odds(dice, turns = 1000000):
    double_rolls = 0
    player_location = 0
    player_active = True
    die_1, die_2 = None, None
    movement = 0
    squares = {}
    for i in range(40):
        squares[i] = 0

    #card stacks
    community_chest = [None for x in range(16)]
    community_chest[0] = 0; community_chest[1] = 10
    community_chest_stack_location = 0; community_chest_card = None
    random.shuffle(community_chest)
    chance = [None for x in range(16)]
    chance[1] = 0; chance[2] = 10; chance[3] = 11; chance[4] = 24; chance[5] = 39; chance[6] = 5
    chance[7] ='NextR'; chance[8] = 'NextR'; chance[9] = 'NextU'; chance[10] = 'Back3'
    chance_stack_location = 0; chance_card = None
    random.shuffle(chance)


    for i in range(turns):
        player_active = True
        die_1 = random.randint(1,dice)
        die_2 = random.randint(1,dice)

        if turns%100 == 0:
            random.shuffle(community_chest)
            random.shuffle(chance)

        #check for 3 consecutive doubles
        if die_1 == die_2:
            double_rolls += 1
            if double_rolls == 3:
                player_location = 10
                player_active = False

        else:
            double_rolls = 0

        if player_active is True:
            player_location = (player_location + die_1 + die_2) % 40

            #Chance landing rules
            if player_location in [7,22,36]:
                chance_card = chance[chance_stack_location]
                if isinstance(chance_card,int):
                    player_location = chance_card
                if isinstance(chance_card, str):
                    if chance_card == 'Back3':
                        player_location -= 3
                    if chance_card == 'NextU':
                        if player_location == 7:
                            player_location = 12
                        if player_location == 22:
                            player_location = 28
                        if player_location == 36:
                            player_location = 12
                    if chance_card == 'NextR':
                        if player_location == 7:
                            player_location = 15
                        if player_location == 22:
                            player_location = 25
                        if player_location == 36:
                            player_location = 5
                chance_stack_location = (chance_stack_location + 1) % 16
                # Community Chest landing rules
                #chance landing at 36 and drawing back 3 can result in community chest on 33
                if player_location in [2, 17, 33]:
                    community_chest_card = community_chest[community_chest_stack_location]
                    if isinstance(community_chest_card, int):
                        player_location = community_chest_card

                    community_chest_stack_location = (community_chest_stack_location + 1) % 16


        squares[player_location] += 1

    biggest_three = [[0,0],[0,0],[0,0]]
    for i in squares:
        print(i, str(100 * squares[i]/turns)+ '%')
        if squares[i] > biggest_three[0][1] and squares[i] > biggest_three[1][1] and squares[i] > biggest_three[2][1]:
            biggest_three[0][0] = i
            biggest_three[0][1] = squares[i]
        elif squares[i] > biggest_three[1][1] and squares[i] > biggest_three[2][1]:
            biggest_three[1][0] = i
            biggest_three[1][1] = squares[i]
        elif squares[i] > biggest_three[2][1]:
            biggest_three[2][0] = i
            biggest_three[2][1] = squares[i]
    print(biggest_three)






monopoly_odds(6)
