import time
import random
from setting.text_assets import intro, alcoholable_text, gameStart, game_over
from setting.party_setting import initialize_party, update_drink_status, check_game_over
from setting.game_logic import play_game, except_input

from games.game_se import *
from games.game_ek import *
from games.game_wj import *
from games.UpDownGame import *
from games.Game3_JW import *





def main():
    print(intro)
    participant_name = input("비밀 술파티에 오신 당신의 이름은? ")

    print(alcoholable_text)
    alcoholforce = except_input("당신의 주량은 몇 잔인가요? (1~5 선택): ", 5)
    num_friends = except_input("함께 취할 친구는 얼마나 필요하신가요? (최대 3명): ", 3)

    # 파티 초기화
    party_members = initialize_party(participant_name, alcoholforce, num_friends)

    print("\n비밀 술파티 참가자 리스트:")
    for name, info in party_members.items():
        print(f"{name}: 주량 {info['주량']}잔")
    print(gameStart)
    time.sleep(1)

    game_turn = 0
    players = list(party_members.keys())

    while True:
        selector = players[game_turn % len(players)]
        print("==========================================")
        update_drink_status(party_members)

        gameNum = play_game(selector, participant_name)
        print(f"{selector} 님이 {gameNum}번 게임을 선택했습니다.")
        time.sleep(1)

    # guide
    # --------------------------
    # 여기 아래에 각자 게임 추가
    # 인자로 받을 수 있는 변수들
    
    # participant_name - 플레이어 이름 (str)
    # party_members - {참가자 이름: 주랑, 현재 마신 잔 수} 가 저장돼있는 딕셔너리 (dic)
    # players - 참가자들 이름만 들어있는 list (list)
    # num_friends - 게임에 참가중인 인원이 아니라 봇들의 수 (참가 인원 -1) (int)

        if gameNum == 1: # 369게임
            loser = game_369(players, participant_name)
        elif gameNum == 2: # 숫자 맞추기 게임
            loser = up_down_game(participant_name, players)
        elif gameNum == 3: # 반응속도 게임
            loser = Game_3(participant_name, party_members)
        elif gameNum == 4: # 랜덤 룰렛 게임
            loser = roulette_game(party_members, players)
        else: # 아파트
            loser = apt_game(participant_name, players)
            
        # party_members[loser]["현재 마신 잔"] += 1
        # print(f"{loser} 한잔 마셔~")

        # 다중 loser 처리
        if isinstance(loser, list):  # 반환된 값이 리스트인 경우
            for l in loser:
                party_members[l]["현재 마신 잔"] += 1
                print(f"{l} 한잔 마셔~")
        else:  # 단일 값인 경우
            party_members[loser]["현재 마신 잔"] += 1
            print(f"{loser} 한잔 마셔~")
            

        if check_game_over(party_members):
            print(game_over)
            break

        next_game = input("\n다음 게임을 진행하시겠습니까?(끝내려면 q 입력, 계속하려면 엔터 입력): ")
        if next_game.lower() == 'q':
            print(f"\n얘들아 {participant_name} 집간대~~ 우~~~")
            print(game_over)
            break

        game_turn += 1

if __name__ == "__main__":
    main()