# 1번 369게임
import random
import math

# 아래는 테스트를 위해서 임의로 지정해 둔 변수 (=> 병합할때 삭제예정)
player = '규일'
mems = ['은경','시은','주원']
mems.append(player)

# 주요 코드
def game_369(member_list):
    print("369 ~ 369! 369 ~ 369!!")
    num = 0 # 현재 부를 숫자 (멤버 인덱스로도 동시에 활용할 예정)
    member_count = len(member_list) # 멤버 수
    while True:
        if not say(member_list[num%member_count], num+1):
            print(f"이번 게임 패자 : {member_list[num%member_count]}")
            return(member_list[num%member_count])
        else:
            num+=1
                
def say(member, num):
    response = ''
    if member == player:
        response = playerTurn(num)
        print(f"{member} : {response}")
    else:
        response = computerTurn(num)
        print(f"{member} : {response}")
    return(isCorrect(num,response))


def playerTurn(num):   # player턴에는 직접 입력을 받음
    while True:
        try:
            choice = int(input(f"당신의 차례입니다! 어떻게 하시겠습니까?? [ 1: (숫자{num} 외치기) | 2: (박수 한번) | 3: (박수 두번) | 4: (박수 세번) ]  : "))
        except(Exception):
            print("그런 선택지는 없다... 1~4번 선택지에서 고르자...")
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
        if p <= 99:
            return(num)
        else:
            return("짝!")
    elif count == 1:
        if p <= 99:
            return("짝!")
        else:
            return(num)
    elif count == 2:
        if p <= 99:
            return("짝짝!")
        else:
            return(num)
    else:
        if p <= 99:
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

game_369(mems)