import random
import time

updown_logo = f"""
======================================================================================================================
 __    __  .______    _______    ______   ____    __    ____ .__   __.      _______      ___      .___  ___.  _______ 
|  |  |  | |   _  \  |       \  /  __  \  \   \  /  \  /   / |  \ |  |     /  _____|    /   \     |   \/   | |   ____|
|  |  |  | |  |_)  | |  .--.  ||  |  |  |  \   \/    \/   /  |   \|  |    |  |  __     /  ^  \    |  \  /  | |  |__   
|  |  |  | |   ___/  |  |  |  ||  |  |  |   \            /   |  . `  |    |  | |_ |   /  /_\  \   |  |\/|  | |   __|  
|  `--'  | |  |      |  '--'  ||  `--'  |    \    /\    /    |  |\   |    |  |__| |  /  _____  \  |  |  |  | |  |____ 
 \______/  | _|      |_______/  \______/      \__/  \__/     |__| \__|     \______| /__/     \__\ |__|  |__| |_______|
======================================================================================================================
"""

updown_intro = f"""
----------------------UpDown 게임 룰----------------------

1. 1~100 사이 어딘가에 있는 숫자를 맞춰야 한다.

2. 첫번째 사람부터 순서대로 숫자를 말한다.

3-1. 말한 숫자가 목표보다 작으면 사회자가 Up이라고 말해준다.

3-2. 말한 숫자가 목표보다 크면 사회자가 Down이라고 말해준다.

4. 정답을 맞춘 사람의 앞사람이 벌칙을 받는다.

---------------------------------------------------------
"""
    
    

def up_down_game(participant_name, players, num_players):
    print(updown_logo)
    time.sleep(2)
    print(updown_intro)
    time.sleep(3)
    
    # 1~100 사이의 목표 숫자를 설정
    updown_number = random.randint(1, 100)
    updown_turn = 0
    updown_min = 0
    updown_max = 101
    
    # 게임 시작
    while True:
        # 현재 차례의 플레이어 이름
        updown_current_player = players[updown_turn % num_players]
        
        # 플레이어가 숫자를 입력
        if updown_current_player == participant_name:
            try:
                print(f"현재 범위: {updown_min+1}~{updown_max-1}")
                updown_guess = int(input(f"이번 차례는 {updown_current_player}!! 숫자는?!?! : "))
                
                # 범위 밖을 입력하면
                if updown_guess < updown_min or updown_guess > updown_max:
                    print(f"숫자는 {updown_min}~{updown_max} 이야")
                    continue
            except ValueError:
                print("숫자를 말해야지!!!")
                continue
        else: # 봇 차례일 때
            updown_guess = random.randint(updown_min + 1, updown_max - 1)
            print(f"{updown_current_player}: 나는 {updown_guess}!")
        time.sleep(1.5)    

        # 숫자 비교
        if updown_guess < updown_number:
            print("\nUP! 정답은 누가 맞추게 될까?\n")
            updown_min = updown_guess
        elif updown_guess > updown_number:
            print("\nDOWN! 아까워~~\n")
            updown_max = updown_guess
        else:
            print("\n*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==")
            print(f"정답입니다! {updown_current_player}이(가) 목표 숫자 {updown_number}을 맞췄다!!\n")
            print(f"{players[(updown_turn-1) % num_players]} 마셔🍺🍺")
            print("*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==\n")
            return players[(updown_turn-1) % num_players]  # 당첨자 반환
        print("=====================================================================\n")
        time.sleep(2)
        # 다음 차례로 이동
        updown_turn += 1
