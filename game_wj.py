import random

# 아래는 테스트를 위해서 임의로 지정해 둔 변수 (=> 병합할때 삭제예정)
player = '규일'
mems = ['은경','시은','주원']
mems.append(player)

# 주요 코드
def game_369(member_list):
    print("369 369! 369 369!!")
    num = 0 # 현재 부를 숫자 (멤버 인덱스로도 동시에 활용할 예정)
    member_count = len(member_list) # 멤버 수
    while True:
        num%=member_count
        if not say(member_list[num], num+1):
            print(f"이번 게임 패자 : {member_list[num]}")
            return(member_list[num])
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
        choice = int(input(f"당신의 차례입니다! 어떻게 하시겠습니까?? [ 1: {num} | 2: (박수 한번) | 3: (박수 두번) | 4: (박수 세번) ]  : "))
        if choice == 1:
            return(num)
        elif choice == 2:
            return("짝")
        elif choice == 3:
            return("짝짝")
        elif choice == 4:
            return("짝짝짝")
        else:
            print("그런 선택지는 없다... 1~4번 선택지에서 고르자...")


def computerTurn(num): # computer턴에는 일정 확률에 따른 대답을 함
    # ex) 숫자만 말해야 하는 상황 (ex.15) 일때는 95%확률로 숫자를, 5%확률로 박수한번을 말함
    # ex) 박수를 n번만 쳐야 하는 상황 (ex.23) 일때는 95%확률로 박수 n번을, 5%확률로 숫자를 말함
    # random.randint(1,100)으로 설정해서 1~95는 정답말하고, 96~100이 걸리면 오답을 말하도록 설정하자
    # isCorrect에 구현한 판단 로직을 이 함수에도 똑같이 넣으면 숫자인지, 혹은 박수n번인지 구별할 수 있음

def isCorrect(num,response):    # 말한 대답이 옳은 대답인지 판단하는 함수
    # 구별하는 방법 :
    # 1. 숫자 자릿수에 따라서 10으로 모듈러 연산 수행
    # 2. 3,6,9중에 하나가 나오면 count를 1씩 증가시킴
    # => 아니면 숫자를 문자열로 받아서 하나씩 읽으면서 판단해도됨. (=> 이게 더 편할듯)
    # 졸려서 나머진 이따가 할게요...


game_369(mems)