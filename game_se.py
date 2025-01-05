#5번 아파트게임
import random

def apt_game(my_turn, num_player, players) :
    #인트로
    print("아파트~ 아파트~ 아파트~ 아파트~")  #인트로
    #층수제한
    limit_floors = (num_player*2)*5
    #층수 입력
    while True :
        target_floor = int(input(f'{my_turn} : ')) 

        if target_floor > limit_floors :
            print(f'빠른 진행을 위해 {limit_floors}층 안에서 골라주세요~')
        elif target_floor<=num_player*2 :
            print(f'노잼~ 더 높은 층으로~')
        else:
            break

    #각 플레이어에게 층수 부여 (전체 층수에서 나머지로 당첨자 선정)
    base_floor = list(range(1, (num_player*2)+1))
    random.shuffle(base_floor) 
    player_hands = {player : [] for player in players}
    for i, floor in enumerate(base_floor):
        player = players[i%num_player]
        player_hands[player].append(floor)


    for player, hand in player_hands.items():
            print(f"{player}: {hand}") 



    calc_floor = (target_floor%(num_player*2))
    if calc_floor == 0:
        calc_floor = num_player*2
    for player, hand in player_hands.items():
        if calc_floor in hand:
            return player







