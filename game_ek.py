# 랜덤 룰렛 게임 : 랜덤으로 누가 술을 마실지 결정하는 게임
# random.choice()로 마실 사람 선택.

import random

def roulette_game():
    players = input("참가자 이름을 쉼표로 구분해서 입력하세요 (예: 철수, 영희, 민수): ").split(",")
    print("\n랜덤 룰렛 게임 시작!!")
    while True:
        input("Enter를 누르면 마실 사람이 정해집니다 (종료하려면 'exit' 입력): ")
        chosen = random.choice(players).strip()
        print(f"{chosen}님! 한 잔 마셔주세요! 🍻")
        if input("계속하려면 Enter, 종료하려면 'exit' 입력: ").lower() == 'exit':
            break

roulette_game()
