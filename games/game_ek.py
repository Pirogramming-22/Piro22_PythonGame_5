# 랜덤 룰렛 게임 : 랜덤으로 누가 술을 마실지 결정하는 게임
# random.choice()로 마실 사람 선택.

import random
import time
from collections import Counter

def roulette_game(participant_name, party_members, players):
    if not players:
        print("참가자가 없습니다. 게임을 종료합니다.")
        return

    print("\n랜덤 룰렛 게임 시작!!")
    chosen_list = []  # 뽑힌 참가자를 저장할 리스트

    for i in range(1, 11):
        time.sleep(1)  # 1초 간격으로 출력
        chosen = random.choice(players).strip()
        chosen_list.append(chosen)
        
        # 현재까지 뽑힌 참가자 출력
        print(f"{i}번: {chosen}")
    
     # Enter 키를 눌러 최종 집계 출력
    input("\n10번의 선택이 끝났습니다. 최종 집계를 보려면 Enter를..!!")

    # 최종 집계
    print("\n=== 최종 집계 ===")
    chosen_counts = Counter(chosen_list)
    for person, count in chosen_counts.items():
        print(f"{person}: {count}번")

    
    # Enter 키를 눌러 결과 표시
    input("\n결과를 보려면 Enter를..! (두구두구두구두구)")
    
    # 가장 많이 지목된 사람 찾기
    max_count = max(chosen_counts.values())
    most_chosen = [person for person, count in chosen_counts.items() if count == max_count]

    # if len(most_chosen) == 1:
    #     # 한 명만 가장 많이 지목된 경우
    #     print(f"\n{most_chosen[0]}가 {max_count}번 지목되어 걸렸네~ 한 잔 마셔~ 🍻")
    # else:
    #     # 동률이 발생한 경우
    #     print("동률이 발생했네~ 술병게임 가보자고~")
    #     print("\n술병 돌려 돌려~~ 술병 돌려 걸리는 사람이 한 잔해~~")
    #     chosen_one = random.choice(most_chosen)
    #     print(f"{', '.join(most_chosen)} 중에서 {chosen_one}! 한 잔 마셔~ 🍻")

    if len(most_chosen) == 1:
        most_chosen = most_chosen[0]  # 리스트가 아닌 문자열로 변경
        print(f"\n{most_chosen}가 {max_count}번 지목되어 걸렸네~ 한 잔 마셔~ 🍻")
    else:
        print("동률이 발생했네~ 술병게임 가보자고~")
        print("\n술병 돌려 돌려~~ 술병 돌려 걸리는 사람이 한 잔해~~")
        most_chosen = random.choice(most_chosen)  # 동률 중 랜덤으로 한 명 선택
        print(f"{', '.join(most_chosen)} 중에서 {most_chosen}! 한 잔 마셔~ 🍻")


    # 술잔 수 업데이트
    party_members[most_chosen]["현재 마신 잔"] += 1

    # 치사량 확인
    if party_members[most_chosen]["현재 마신 잔"] > party_members[most_chosen]["주량"]:
        print(f"\n⚠️ {most_chosen}는 주량 {party_members[most_chosen]['주량']}잔을 초과했습니다. 게임에서 탈락합니다! ⚠️")
        players.remove(most_chosen)  # 플레이어 리스트에서 제거
        return most_chosen  # 탈락자 반환

    return most_chosen  # 술을 마신 참가자 반환



if __name__ == "__main__":
    # 참가자 리스트 입력
    print("참가자 이름을 입력하세요 (쉼표로 구분):")
    participants_input = input()
    participants = [name.strip() for name in participants_input.split(",") if name.strip()]

    if not participants:
        print("참가자가 없습니다. 프로그램을 종료합니다.")
    else:
        roulette_game(participants)
