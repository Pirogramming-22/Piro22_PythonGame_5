import random
import time
from setting.text_assets import updown_logo, updown_intro

def up_down_game(participant_name, players):
    print(updown_logo)
    time.sleep(2)
    print(updown_intro)
    time.sleep(3)
    
    # 1~100 사이의 목표 숫자를 설정
    updown_number = random.randint(1, 100)
    updown_turn = 0
    updown_min = 0
    updown_max = 101
    num_players = len(players)
    # 게임 시작
    while True:
        # 현재 차례의 플레이어 이름
        updown_current_player = players[updown_turn]
        
        # 플레이어가 숫자를 입력
        if updown_current_player == participant_name:
            try:
                print(f"현재 범위: {updown_min+1}~{updown_max-1}")
                updown_guess = int(input(f"이번 차례는 {updown_current_player}!! 숫자는?!?! : "))
                
                # 범위 밖을 입력하면
                if updown_guess <= updown_min or updown_guess >= updown_max:
                    
                    print(f"숫자는 {updown_min+1}~{updown_max-1} 이야")
                    print(f"바보샷~!~! 바보샷~!~!")
                    print("""
🤪 축하합니다~!! 🎉
이 게임에서 바보가 된 사람은~~
바로 너~!! 🏆
바보가 고른 게임은 할 수 없어~!! 
게임 체~인지~~!! 😝😝
                          """)
                    return participant_name
            except ValueError:
                print("너 취했어? 숫자를 말해야지!!!")
                print(f"바보샷~!~! 바보샷~!~!")
                print("""
🤪 축하합니다~!! 🎉
이 게임에서 바보가 된 사람은~~
바로 너~!! 🏆
바보가 고른 게임은 할 수 없어~!! 
게임 체~인지~~!! 😝😝
                          """)
                return participant_name
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
        updown_turn = updown_turn % num_players
