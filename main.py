import random
import time

# 텍스트들
intro = f"""
 ______                                   ______                ____                        ___       ____                                     
/\__  _\                                 /\  ___\              /\  _`\                     /\_ \     /\  _`\                                   
\/_/\ \/     __      __       ___ ___    \ \ \__/              \ \,\L\_\     ___     ___   \//\ \    \ \ \L\_\     __       ___ ___       __   
   \ \ \   /'__`\  /'__`\   /' __` __`\   \ \___``\             \/_\__ \    / __`\  / __`\   \ \ \    \ \ \L_L   /'__`\   /' __` __`\   /'__`\ 
    \ \ \ /\  __/ /\ \L\.\_ /\ \/\ \/\ \   \/\ \L\ \              /\ \L\ \ /\ \L\ \/\ \L\ \   \_\ \_   \ \ \/, \/\ \L\.\_ /\ \/\ \/\ \ /\  __/ 
     \ \_\\\\ \____\\\\ \__/.\_\\\\ \_\ \_\ \_\   \ \____/              \ `\____\\\\ \____/\ \____/   /\____\   \ \____/\ \__/.\_\\\\ \_\ \_\ \_\\\\ \____\\
      \/_/ \/____/ \/__/\/_/ \/_/\/_/\/_/    \/___/                \/_____/ \/___/  \/___/    \/____/    \/___/  \/__/\/_/ \/_/\/_/\/_/ \/____/
==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*
ᕕ(ᐛ)ᕗ   ᕕ(ᐛ)ᕗ   ᕕ(ᐛ)ᕗ   ᕕ(ᐛ)ᕗ   ᕕ(ᐛ)ᕗ   ᕕ(ᐛ)ᕗ 5조와 함께하는 랜덤 게임~~ ᕕ(ᐛ)ᕗ ᕕ(ᐛ)ᕗ ᕕ(ᐛ)ᕗ ᕕ(ᐛ)ᕗ ᕕ(ᐛ)ᕗ ᕕ(ᐛ)ᕗ ᕕ(ᐛ)ᕗ ᕕ(ᐛ)ᕗ ᕕ(ᐛ)ᕗ ᕕ(ᐛ)ᕗ ᕕ(ᐛ)ᕗ 
==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*
"""
alcoholable_text = f"""
~~~~~~~~~~~~~~~~~~~~~~~~당신의 주량은?~~~~~~~~~~~~~~~~~~~~~~~~
                    🍺 1. 소주 반병 (2잔)
                    🍺 2. 소주 반병에서 한병 (4잔)                
                    🍺 3. 소주 한병에서 한병 반 (6잔)                
                    🍺 4. 소주 한병 반에서 두병 (8잔)                
                    🍺 5. 소주 두병 이상 (10잔)       
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                    
"""

game_list = f"""
~~~~~~~~~~~~~~~~~~~~~~~~오늘의 술게임~~~~~~~~~~~~~~~~~~~~~~~~
                    🍺 1. 369게임
                    🍺 2. 숫자 맞추기 게임              
                    🍺 3. 반응속도 게임              
                    🍺 4. 랜덤 룰렛 게임              
                    🍺 5. 아파트    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~            
"""

gameStart = f"""
 ____                                                 ____        __                        __      
/\  _`\                                              /\  _`\     /\ \__                    /\ \__   
\ \ \L\_\     __       ___ ___       __              \ \,\L\_\   \ \ ,_\     __      _ __  \ \ ,_\  
 \ \ \L_L   /'__`\   /' __` __`\   /'__`\             \/_\__ \    \ \ \/   /'__`\   /\`'__\ \ \ \/  
  \ \ \/, \/\ \L\.\_ /\ \/\ \/\ \ /\  __/               /\ \L\ \   \ \ \_ /\ \L\.\_ \ \ \/   \ \ \_ 
   \ \____/\ \__/.\_\\\\ \_\ \_\ \_\\\\ \____\              \ `\____\   \ \__\\\\ \__/.\_\ \ \_\    \ \__\\
    \/___/  \/__/\/_/ \/_/\/_/\/_/ \/____/               \/_____/    \/__/ \/__/\/_/  \/_/     \/__/
"""

# 봇들 주량 설정
bots = {
    name: random.choice([2, 4, 6, 8, 10]) for name in {"원준봇", "규일봇", "주원봇", "은경봇", "시은봇"}
}

print(intro)
participant = input("비밀 술파티에 오신 당신의 이름은? ")
print(alcoholable_text)
while True: # 주량 입력 예외처리
    try:
        alcoholforce = int(input("당신의 주량은 몇 잔인가요? (1~5 선택) : "))
        if 1 <= alcoholforce <= 5:
            break  # 올바른 입력이면 루프 종료
        else:
            print("1에서 5 사이의 숫자여야 합니다. 다시 입력해주세요.")
    except ValueError:
        print("1에서 5 사이의 숫자여야 합니다. 다시 입력해주세요.")

# 게임 참가자 인원수 입력 예외처리
while True:
    try:
        NumOfPart = int(input("함께 취할 친구는 얼마나 필요하신가요? (최대 5명): "))
        if 1 <= NumOfPart <= 5:
            break
        else:
            print("1에서 5 사이의 숫자여야 합니다. 다시 입력해주세요.")
    except ValueError:
        print("1에서 5 사이의 숫자여야 합니다. 다시 입력해주세요.")
        
# 참가할 봇 선정
selected_bots = random.sample(list(bots.items()), NumOfPart)

NumOfPart += 1 # 본인 추가

# 게임 참가자 딕셔너리 생성
party_members = {
    participant: {"주량": alcoholforce * 2, "현재 마신 잔": 0}
}

for bot_name, bot_alcohol in selected_bots: # 딕셔너리에 할당
    party_members[bot_name] = {"주량": bot_alcohol, "현재 마신 잔": 0}

time.sleep(1)
print("\n비밀 술파티 참가자 리스트:") # 참가자 리스트 출력
print("=====================")
for name, info in party_members.items():
    print(f"{name}: 주량 {info['주량']}잔")
print("=====================")
time.sleep(1)
print(gameStart)
time.sleep(1)



#  게임 시작
game_turn = 0
players = list(party_members.keys())
while True:
    selector = players[game_turn % len(players)]  # 게임 선택할 사람 선정 (순차적으로 돌아감)
    
    print("==========================================") # 주량, 남은 주량 출력
    for name, info in party_members.items():
        print(f"{name}: 주량 {info['주량']}잔, 현재 몇잔? {info['현재 마신 잔']}잔")
    print("==========================================")
    
    if selector == participant: # 선택자가 본인이면 입력받기
        while True: #예외 처리
            try:
                print(game_list)
                gameNum = int(input(f"{participant}(이)가 좋아하는 랜덤 게임~ 무슨 게임? : "))
                if 1 <= alcoholforce <= 5:
                    break  # 올바른 입력이면 루프 종료
                else:
                    print("게임은 5개밖에 없어!")
            except ValueError:
                print("숫자로 말해야지!")
    else:
        print(game_list)
        print(f"{selector}(이)가 좋아하는 랜덤 게임~ 무슨 게임? : ")
        print("==========================================")
        gameNum = random.randint(1, 5);
        time.sleep(1)
    print(f"{selector} 님이 {gameNum}번 게임을 선택했습니다.")
    print("==========================================")
    time.sleep(1)
  
    if gameNum == 1: # 369게임
        loser = participant
    elif gameNum == 2: # 숫자 맞추기 게임  
        loser = participant
    elif gameNum == 3: # 반응속도 게임 
        loser = participant
    elif gameNum == 4: # 랜덤 룰렛 게임  
        loser = participant
    else: # 아파트
        loser = participant
    
    print(f"{loser} 한잔 마셔~")
    
    party_members[loser]["현재 마신 잔"] += 1
    # 게임 종료
    for name, info in party_members.items():
        if info["현재 마신 잔"] > info["주량"]:
            print()
            print("⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️")
            print(f"{name} 님이 쓰러졌습니다! 게임 종료!")
            print("⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️")
            exit()
    
    game_turn += 1
    
    
    
    
        
        






