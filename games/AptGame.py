#5번 아파트게임
import random
import time
from setting.text_assets import apt_logo, apt_intro

def apt_game(my_turn, players) :
    print(apt_logo)
    time.sleep(2)
    print(apt_intro)
    time.sleep(2)

    #인트로
    print("아파트~ 아파트~ 아파트~ 아파트~")  #인트로
    num_player = len(players)
    #층수제한
    limit_floors = (num_player*2)*3
    #층수 입력
    while True :
        print(f"스겜을 위해서 최대 몇층~? {limit_floors}층!")
        try:
            target_floor = int(input(f'{my_turn} : '))
            print("")
            if target_floor > limit_floors :
                print(f'최대 {limit_floors}층이라니까~ 바보')
                print("""
                🤪 축하합니다~!! 🎉
                이 게임에서 바보가 된 사람은~~
                바로 너~!! 🏆 
                바보가 고른 게임은 할 수 없어~!! 
                게임 체~인지~~!! 😝😝 
                """)
                print(f"{my_turn} 바보 마셔!")
                time.sleep(1.5)
                return my_turn
            elif target_floor<=num_player*2 :
                print(f'우우...다음엔 펜트하우스에 살아보자...')
                print("""
                🤪 축하합니다~!! 🎉
                이 게임에서 바보가 된 사람은~~
                바로 너~!! 🏆 
                바보가 고른 게임은 할 수 없어~!! 
                게임 체~인지~~!! 😝😝 
                """)
                print(f"{my_turn} 바보 마셔!")
                time.sleep(1.5)
                return my_turn
            else:
                break
        except(Exception):
                print(f"{my_turn} : 어..어...아악..! (실수로 얼타버렸다...)")
                time.sleep(1)
                print("""
                🤪 축하합니다~!! 🎉
                이 게임에서 바보가 된 사람은~~
                바로 너~!! 🏆 
                바보가 고른 게임은 할 수 없어~!! 
                게임 체~인지~~!! 😝😝 
                """)
                time.sleep(1.5)
                print(f"{my_turn} 바보 마셔!")
                return my_turn


    #각 플레이어에게 층수 부여 (전체 층수에서 나머지로 당첨자 선정)
    base_floor = list(range(1, (num_player*2)+1))
    random.shuffle(base_floor) 
    player_hands = {player : [] for player in players}
    for i, floor in enumerate(base_floor):
        player = players[i%num_player]
        player_hands[player].append(floor)

    #배정된 층 말하기
    floor_to_player = {floor: player for player, hand in player_hands.items() for floor in hand}
    sorted_floors = sorted(floor_to_player.keys()) 

    for i in range(1, target_floor + 1):
        assigned_floor = (i - 1) % len(sorted_floors) + 1  
        player = floor_to_player[sorted_floors[(i - 1) % len(sorted_floors)]]  
        print(f"{player} : {i}층")  
        time.sleep(0.6)

    print("")

    calc_floor = (target_floor%(num_player*2))
    
    if calc_floor == 0:
        calc_floor = num_player*2
    for player, hand in player_hands.items():
        if calc_floor in hand:
            print(f"와~ {player} 걸렸다!!")
            print(f"{player} 마셔🍺🍺")
            return player







