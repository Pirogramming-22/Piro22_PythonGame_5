# input manage 파일

import random
from setting.text_assets import game_list

# 게임 선택
def play_game(selector, participant):
    if selector == participant:
        while True:
            try:
                print(game_list)
                gameNum = int(input(f"{participant}(이)가 좋아하는 랜덤 게임~ 무슨 게임? : "))
                if 1 <= gameNum <= 5:
                    return gameNum
                else:
                    print("게임은 5개밖에 없어!")
            except ValueError:
                print("숫자로 말해야지!")
    else:
        print(game_list)
        print(f"{selector}(이)가 좋아하는 랜덤 게임~ 무슨 게임? : ")
        gameNum = random.randint(1, 5)
        return gameNum

# input 예외처리
def except_input(prompt, max_num):
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= max_num:
                return value
            else:
                print(f"1 ~ {max_num} 사이의 숫자여야 합니다. 다시 입력해주세요.")
        except ValueError:
            print(f"1~{max_num} 사이의 숫자여야 합니다. 다시 입력해주세요.")
