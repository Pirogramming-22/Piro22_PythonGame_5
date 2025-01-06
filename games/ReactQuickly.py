import random
import time
from setting.text_assets import game3_intro, game3_rule


import random
import time
from setting.text_assets import game3_intro, game3_rule


def Game_3(player_name, party_members):
    round_number = 1  # 라운드 번호 관리

    print(game3_intro)
    time.sleep(2)

    while True:  # 실패자가 나올 때까지 반복
        print(game3_rule)
        time.sleep(5)
        print(f"\n{'='*40} Round {round_number} {'='*40}\n")

        # 실패자 리스트
        losers = []  # 여러 실패자를 저장하기 위한 리스트

        # 플레이어 정보 추출
        player_drinks = party_members[player_name]["현재 마신 잔"]
        player_limit = party_members[player_name]["주량"]

        # 다른 참가자 정보
        participants = [
            {"name": name, "drinks": info["현재 마신 잔"], "limit": info["주량"]}
            for name, info in party_members.items()
            if name != player_name
        ]

        # 플레이어 차례
        print(f"\n[이번 순서는] {player_name}의 차례입니다. 준비...")
        time.sleep(random.uniform(2, 5))
        signal = random.choice(["GO!", "숫자"])

        if signal == "GO!":
            print(signal)
            reaction_start = time.time()
            user_input = input(">> (엔터로 반응) ")
            reaction_time = time.time() - reaction_start

            if user_input == "" and reaction_time <= 0.5:
                print(f"성공! 반응 시간: {reaction_time:.2f}초")
            else:
                print(f"실패! 반응이 느리거나 잘못되었습니다. 반응 시간: {reaction_time:.2f}초")
                print(f"{player_name} 한 잔 마셔!")
                losers.append(player_name)  # 실패자를 리스트에 추가

        elif signal == "숫자":
            target_number = random.randint(1, 5)
            print(f">> (2초 안에 {target_number}을(를) 입력하세요!)")
            reaction_start = time.time()
            user_input = input(">> ")

            if (
                time.time() - reaction_start >= 2
                or not (user_input.isdigit() and int(user_input) == target_number)
            ):
                print(f"실패! {target_number}을(를) 입력하지 않았거나 시간이 초과되었습니다.")
                print(f"{player_name} 한 잔 마셔!")
                losers.append(player_name)  # 실패자를 리스트에 추가
            else:
                print(f"성공! 정확히 {target_number}을(를) 입력했습니다.")

        # 참가자 차례
        for participant in participants:
            print(f"\n[이번 순서는] {participant['name']}의 차례입니다. 준비...")
            time.sleep(random.uniform(2, 5))
            signal = random.choice(["GO!", "숫자"])

            if signal == "GO!":
                success = random.choice([True, False])
                if success:
                    print(f"{participant['name']} 성공! 빠르게 반응했습니다.")
                else:
                    print(f"{participant['name']} 실패! 반응이 느렸습니다.")
                    print(f"{participant['name']} 한 잔 마셔!")
                    losers.append(participant["name"])  # 실패자를 리스트에 추가

            elif signal == "숫자":
                target_number = random.randint(1, 5)
                success = random.choice([True, False])
                if success:
                    print(f"{participant['name']} 성공! {target_number}을(를) 정확히 입력했습니다.")
                else:
                    print(f"{participant['name']} 실패! 숫자를 잘못 입력했습니다.")
                    print(f"{participant['name']} 한 잔 마셔!")
                    losers.append(participant["name"])  # 실패자를 리스트에 추가

        # 실패자 처리
        if losers:
            print(f"\n이번 라운드에서 실패자: {', '.join(losers)}")
            return losers  # 실패자 리스트 반환

        # 모든 참가자가 성공한 경우
        print("\n모두 성공했습니다! 다음 라운드로 넘어갑니다.\n")
        round_number += 1  # 다음 라운드로 이동
