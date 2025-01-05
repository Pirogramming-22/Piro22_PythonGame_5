# 랜덤 룰렛 게임 : 랜덤으로 누가 술을 마실지 결정하는 게임
# random.choice()로 마실 사람 선택.

import random

def roulette_game(players):
    if not players:
        print("참가자가 없습니다. 게임을 종료합니다.")
        return

    print("\n랜덤 룰렛 게임 시작!!")
    while True:
        user_input = input("Enter를 누르면 마실 사람이 정해집니다 (종료하려면 'exit' 입력): ").lower()
        if user_input == "exit":
            break
        chosen = random.choice(players).strip()
        print(f"{chosen}! 한 잔 마셔~ 🍻")