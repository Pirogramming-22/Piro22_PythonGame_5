import random

# 파티 초기 설정
def initialize_party(participant, alcoholforce, num_friends):
    bots = {
        name: random.choice([2, 4, 6, 8, 10]) for name in {"원준봇", "규일봇", "주원봇", "은경봇", "시은봇"}
    }
    selected_bots = random.sample(list(bots.items()), num_friends)
    party_members = {
        participant: {"주량": alcoholforce * 2, "현재 마신 잔": 0}
    }
    for bot_name, bot_alcohol in selected_bots:
        party_members[bot_name] = {"주량": bot_alcohol, "현재 마신 잔": 0}
    return party_members

# 현재 주량 출력
def update_drink_status(party_members):
    for name, info in party_members.items():
        print(f"{name}: 주량 {info['주량']}잔, 현재 몇잔? {info['현재 마신 잔']}잔")
    print("==========================================")

# gameover
def check_game_over(party_members):
    for name, info in party_members.items():
        if info["현재 마신 잔"] > info["주량"]:
            print(f"{name} 님이 쓰러졌습니다! 게임 종료!")
            return True
    return False
