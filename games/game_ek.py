# # 랜덤 룰렛 게임 : 랜덤으로 누가 술을 마실지 결정하는 게임
# # random.choice()로 마실 사람 선택.

import random
import time
from collections import Counter

def roulette_game(party_members, players):
    if not players:
        print("참가자가 없습니다. 게임을 종료합니다.")
        return

    print("\n -------------------랜덤 룰렛 게임 룰--------------------")
    print("\n1. 10번 룰렛을 랜덤으로 돌린다.\n ")
    print("2. 가장 많이 걸린 사람이 술 마신다.\n")
    print("3. 단, 동률이 발생할 경우, 술병을 돌려서 걸린 사람이 마신다.\n")
    print("----------------------------------------------------------")
    time.sleep(1)
    print("\n랜덤 룰렛 게임 시작!!")
    chosen_list = []

    for i in range(1, 11):
        time.sleep(1)
        chosen = random.choice(players).strip()
        chosen_list.append(chosen)
        
        print(f"{i}번: {chosen}")
    
    input("\n10번의 선택이 끝났습니다. 최종 집계를 보려면 Enter를..!!")

    print("\n=== 최종 집계 ===")
    chosen_counts = Counter(chosen_list)
    for person, count in chosen_counts.items():
        print(f"{person}: {count}번")

    input("\n결과를 보려면 Enter를..! (두구두구두구두구)")

    max_count = max(chosen_counts.values())
    most_chosen = [person for person, count in chosen_counts.items() if count == max_count]

    if len(most_chosen) == 1:
        chosen_one = most_chosen[0]
        print(f"\n{chosen_one}가 {max_count}번 지목되어 걸렸네~ 한 잔 마셔~ 🍻")
    else:
        print("동률이 발생했네~ 술병게임 가보자고~")
        print("\n술병 돌려 돌려~~ 술병 돌려 걸리는 사람이 한 잔해~~")
        chosen_one = random.choice(most_chosen)
        print(f"{', '.join(most_chosen)} 중에서 {chosen_one}! 한 잔 마셔~ 🍻")

    # 치사량 확인
    if party_members[chosen_one]["현재 마신 잔"] + 1 > party_members[chosen_one]["주량"]:
        print(f"\n⚠️ {chosen_one}는 주량 {party_members[chosen_one]['주량']}잔을 초과했습니다. 게임에서 탈락합니다! ⚠️")
        players.remove(chosen_one)
        return chosen_one

    return chosen_one


if __name__ == "__main__":
    print("참가자 이름을 입력하세요 (쉼표로 구분):")
    participants_input = input()
    participants = [name.strip() for name in participants_input.split(",") if name.strip()]

    if not participants:
        print("참가자가 없습니다. 프로그램을 종료합니다.")
    else:
        party_members = {name: {"주량": random.randint(3, 5), "현재 마신 잔": 0} for name in participants}
        players = participants.copy()

        while players:
            result = roulette_game(party_members, players)
            if result is None:
                break
            print("\n게임을 계속하시겠습니까? (y/n):")
            continue_game = input().strip().lower()
            if continue_game != 'y':
                print("\n게임을 종료합니다. 모두 수고하셨습니다! 🎉")
                break