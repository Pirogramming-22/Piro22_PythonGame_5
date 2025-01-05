import random
import time

def print_game_over(participant_name):
    print("\n" + "=" * 80)
    print(" ██████   █████  ███    ███ ███████     ██████   ██    ██ ███████ ██████  ")
    print("██       ██   ██ ████  ████ ██         ██    ██  ██    ██ ██      ██   ██ ")
    print("██   ███ ███████ ██ ████ ██ █████     ██      ██ ██    ██ █████   ██████  ")
    print("██    ██ ██   ██ ██  ██  ██ ██         ██    ██  ██    ██ ██      ██   ██ ")
    print(" ██████  ██   ██ ██      ██ ███████     ██████     ████   ███████ ██   ██ ")
    print("=" * 80)
    print(f"{participant_name}(이)가 전사했습니다... 꿈나라에서는 편히 쉬시길... zzz")
    print("🍺 다음에 술마시면 또 불러주세요 ~ 안녕 ! 🍺")
    print("=" * 80)


def Game_3(player_name, party_members, players):
    """
    player_name (str): 현재 플레이어 이름
    party_members (dict): {이름: {"주량": int, "현재 마신 잔": int}} 형태의 참가자 정보
    players (list): 참가자 이름 리스트
    """
    # 플레이어 정보 추출
    player_drinks = party_members[player_name]["현재 마신 잔"]
    player_limit = party_members[player_name]["주량"]

    # 다른 참가자 정보
    participants = [
        {"name": name, "drinks": info["현재 마신 잔"], "limit": info["주량"]}
        for name, info in party_members.items()
        if name != player_name
    ]

    print(f"\n🎮 {player_name}의 반응 속도 게임 시작! 🎮")
    print("규칙: - 'GO!'가 나오면 0.5초 이내에 엔터를 입력해야 성공.")
    print("- 숫자가 나오면 2초 안에 지정된 숫자를 입력해야 성공.")
    print("- 실패하면 술을 마십니다. 치사량을 초과하면 게임이 종료됩니다.\n")

    # 랜덤 신호
    signal = random.choice(["GO!", "숫자"])
    wait_time = random.uniform(2, 5)
    print(f"\n[이번 순서는] {player_name}의 차례입니다. 준비...")
    time.sleep(wait_time)

    if signal == "GO!":
        print(signal)
        reaction_start = time.time()
        user_input = input(">> (엔터로 반응) ")
        reaction_time = time.time() - reaction_start

        if user_input == "" and reaction_time <= 0.5:
            print(f"성공! 반응 시간: {reaction_time:.2f}초")
        else:
            print(f"실패! 반응이 느리거나 잘못되었습니다. 반응 시간: {reaction_time:.2f}초")
            player_drinks += 1

    elif signal == "숫자":
        target_number = random.randint(1, 5)
        print(f">> (2초 안에 {target_number}을(를) 입력하세요!)")
        reaction_start = time.time()
        user_input = None

        try:
            user_input = input(">> ")
        except:
            pass

        if time.time() - reaction_start >= 2 or not (user_input and user_input.isdigit() and int(user_input) == target_number):
            print(f"실패! {target_number}을(를) 입력하지 않았거나 시간이 초과되었습니다.")
            player_drinks += 1
        else:
            print(f"성공! 정확히 {target_number}을(를) 입력했습니다.")

    # 플레이어 결과 업데이트
    party_members[player_name]["현재 마신 잔"] = player_drinks

    # 참가자 차례
    for participant in participants:
        signal = random.choice(["GO!", "숫자"])
        print(f"\n[이번 순서는] {participant['name']}의 차례입니다. 준비...")
        time.sleep(wait_time)

        if signal == "GO!":
            success = random.choice([True, False])
            if success:
                print(f"{participant['name']} 성공! 빠르게 반응했습니다.")
            else:
                print(f"{participant['name']} 실패! 반응이 느렸습니다.")
                party_members[participant["name"]]["현재 마신 잔"] += 1

        elif signal == "숫자":
            target_number = random.randint(1, 5)
            success = random.choice([True, False])
            if success:
                print(f"{participant['name']} 성공! {target_number}을(를) 정확히 입력했습니다.")
            else:
                print(f"{participant['name']} 실패! 숫자를 잘못 입력했습니다.")
                party_members[participant["name"]]["현재 마신 잔"] += 1

        # 치사량 확인
        if party_members[participant["name"]]["현재 마신 잔"] > party_members[participant["name"]]["주량"]:
            print_game_over(participant["name"])
            return participant["name"]

    # 현재 플레이어가 치사량 초과인지 확인
    if player_drinks > player_limit:
        print_game_over(player_name)
        return player_name

    # 패자가 없는 경우 None 반환
    return None
