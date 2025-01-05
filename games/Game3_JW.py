# Game3_JW : 반응 속도 테스트 게임

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


def print_final_results(player_name, player_drinks, player_limit, participants):
    """최종 결과 출력 (치사량은 최소 0으로 제한)"""
    print("~" * 50)
    print(f"{player_name}은(는) 지금까지 {player_drinks}🍺! 치사량까지 {max(0, player_limit - player_drinks)}")
    for participant in participants:
        remaining_limit = max(0, participant['limit'] - participant['drinks'])
        print(f"{participant['name']}은(는) 지금까지 {participant['drinks']}🍺! 치사량까지 {remaining_limit}")
    print("~" * 50)


def Game_3(player_name, player_drinks, player_limit, participants):
    """
        player_name (str): 플레이어 이름
        player_drinks (int): 플레이어가 현재까지 마신 잔 수
        player_limit (int): 플레이어의 치사량
        participants (list[dict]): 다른 참가자 정보 (이름과 주량)
    """
    print(f"\n🎮 {player_name}의 반응 속도 게임 시작! 🎮")
    print("규칙: - 'GO!'가 나오면 0.5초 이내에 엔터를 입력해야 성공.")
    print("- 숫자가 나오면 2초 안에 지정된 숫자를 입력해야 성공.")
    print("- 실패하면 술을 마시며, 한 명이라도 치사량에 도달하면 전체 게임이 종료됩니다.\n")

    # 플레이어 차례
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
        target_number = random.randint(1, 5)  # 1~5 중 하나의 숫자 랜덤 선택
        print(f">> (2초 안에 {target_number}을(를) 입력하세요!)")
        reaction_start = time.time()
        user_input = None

        while time.time() - reaction_start < 2:
            try:
                user_input = input(">> ")
                if user_input.isdigit() and int(user_input) == target_number:
                    print(f"성공! 정확히 {target_number}을(를) 입력했습니다.")
                    break
            except:
                pass

        # 결과 판정
        if user_input is None or not (user_input.isdigit() and int(user_input) == target_number):
            print(f"실패! {target_number}을(를) 입력하지 않았거나 시간이 초과되었습니다.")
            player_drinks += 1

    # 참가자 차례
    for participant in participants:
        signal = random.choice(["GO!", "숫자"])
        print(f"\n[이번 순서는] {participant['name']}의 차례입니다. 준비...")
        time.sleep(wait_time)

        if signal == "GO!":
            print(signal)
            success = random.choice([True, False])
            if success:
                print(f"{participant['name']} 성공! 빠르게 반응했습니다.")
            else:
                print(f"{participant['name']} 실패! 반응이 느렸습니다.")
                participant["drinks"] += 1

        elif signal == "숫자":
            target_number = random.randint(1, 5)
            print(f">> (컴퓨터는 {target_number}을(를) 입력해야 성공입니다!)")
            success = random.choice([True, False])
            if success:
                print(f"{participant['name']} 성공! {target_number}을(를) 정확히 입력했습니다.")
            else:
                print(f"{participant['name']} 실패! 숫자를 잘못 입력했습니다.")
                participant["drinks"] += 1


        if participant["drinks"] >= participant["limit"]:
            print_final_results(player_name, player_drinks, player_limit, participants)
            print_game_over(participant["name"])
            return None

    # 결과 반환
    results = {
        "player_name": player_name,
        "player_drinks": player_drinks,
        "player_limit": player_limit,
        "participants": participants,
    }
    return results


# 예시 실행
if __name__ == "__main__":
    # 초기 데이터 설정
    player_name = "Player"
    player_drinks = 0
    player_limit = 5
    participants = [
        {"name": "은서", "drinks": 2, "limit": 3},
        {"name": "예진", "drinks": 0, "limit": 8},
        {"name": "연서", "drinks": 0, "limit": 6},
        {"name": "하연", "drinks": 3, "limit": 7},
    ]

    # 게임 실행
    results = Game_3(player_name, player_drinks, player_limit, participants)

    if results:
        print("~" * 50)
        print(f"{player_name}은(는) 지금까지 {player_drinks}🍺! 치사량까지 {max(0, player_limit - player_drinks)}")
        for participant in participants:
            remaining_limit = max(0, participant['limit'] - participant['drinks'])
            print(f"{participant['name']}은(는) 지금까지 {participant['drinks']}🍺! 치사량까지 {remaining_limit}")
        print("~" * 50)
