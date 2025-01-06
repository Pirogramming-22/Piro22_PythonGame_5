# 1번 369게임
import random
import math
import time
from setting.text_assets import logo_369

# 주요 코드
def game_369(member_list, player):
    showRule()
    print("369 ~ 369! 369 ~ 369!!")
    time.sleep(0.5)
    num = 0 # 현재 부를 숫자 (멤버 인덱스로도 동시에 활용할 예정)
    member_count = len(member_list) # 멤버 수
    while True:
        if not say(member_list[num%member_count], num+1, player):
            print("\n*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==")
            print(f"이번 게임의 패자는 {member_list[num%member_count]}!!!\n")
            print(f"{member_list[num%member_count]} 마셔🍺🍺")
            print("*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==\n")
            return(member_list[num%member_count])
        else:
            num+=1

def showRule():
    print(logo_369)
    time.sleep(1)
    print("\n------------------------------369 게임 룰------------------------------\n")
    print("1. 순서대로 돌아가며 숫자를 말하거나 박수를 치는 게임이다.\n")
    print("2. 숫자 3,6,9 중에 하나라도 들어있다면 들어있는 수만큼 박수를 쳐야한다.\n")
    print("3. 만약 3,6,9 중에 하나라도 포함되어 있지 않다면 그냥 그 숫자를 외친다.\n")
    print("4. 수는 1씩 증가하며, 숫자의 표현방법이 틀린 사람은 패배한다.\n")
    print("EX1) 12에는 하나도 포함되어 있지 않기에 숫자를 그대로 말해야 한다.\n")
    print("EX2) 23에는 숫자 3이 포함되어 있기에 숫자를 말하지 않고 박수를 한 번 쳐야한다.\n")
    print("EX3) 63에는 숫자 6과 3, 총 2개가 포함되어 있기에 숫자를 말하지 않고 박수를 두 번 쳐야한다.\n")
    print("------------------------------------------------------------------------\n")
    time.sleep(2)

def say(member, num, player):
    response = ''
    if member == player:
        response = playerTurn(num)
        print(f"{member} : {response}")
        time.sleep(0.5)
    else:
        response = computerTurn(num)
        print(f"{member} : {response}")
        time.sleep(0.5)
    return(isCorrect(num,response))


def playerTurn(num):   # player턴에는 직접 입력을 받음
    while True:
        try:
            choice = int(input(f"당신의 차례입니다! 어떻게 하시겠습니까?? [ 1: (숫자{num} 외치기) | 2: (박수 한번) | 3: (박수 두번) | 4: (박수 세번) ]  : "))
        except(Exception):
            print("그런 선택지는 없다... 1~4번 선택지에서 고르자...")
            time.sleep(0.5)
            continue
        if choice == 1:
            return(num)
        elif choice == 2:
            return("짝!")
        elif choice == 3:
            return("짝짝!")
        elif choice == 4:
            return("짝짝짝!")
        else:
            print("그런 선택지는 없다... 1~4번 선택지에서 고르자...")


def computerTurn(num): # computer턴에는 일정 확률에 따른 대답을 함
    p = random.randint(1,100)
    count = 0
    for i in range(int(math.log10(num))+1):
        if str(num)[i] == '3' or str(num)[i] == '6' or str(num)[i] == '9':
            count+=1
    if count == 0:
        if p <= 97:
            return(num)
        else:
            return("짝!")
    elif count == 1:
        if p <= 97:
            return("짝!")
        else:
            return(num)
    elif count == 2:
        if p <= 97:
            return("짝짝!")
        else:
            return(num)
    else:
        if p <= 97:
            return("짝짝짝!")
        else:
            return(num)

def isCorrect(num, response):    # 말한 대답이 옳은 대답인지 판단하는 함수
    count = 0
    for i in range(int(math.log10(num))+1):
        if str(num)[i] == '3' or str(num)[i] == '6' or str(num)[i] == '9':
            count+=1
    if count == 0:      # 그냥 숫자인 경우
        if response == num:
            return(True)
        else:
            return(False)
    elif count == 1:    # 박수 1번인 경우
        if response == "짝!":
            return(True)
        else:
            return(False)
    elif count == 2:    # 박수 2번인 경우
        if response == "짝짝!":
            return(True)
        else:
            return(False)
    else:               # 박수 3번인 경우
        if response == "짝짝짝!":
            return(True)
        else:
            return(False)