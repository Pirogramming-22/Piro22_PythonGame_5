# 피로그래밍 2주차 5조 팀과제

## 과제: 혼자하는 python 술게임

**과제 예시**
1. 게임 시작
    - 인트로 출력
2. 사용자 입력
3. 본인 주량 입력
4. 같이 대결할 사람 초대
5. 게임 리스트 출력
6. 게임 선택 - 게임 시작
7. 게임 결과를 반영해 현재 남은 목숨(주량) 출력
8. 한명이 죽으면 게임 오버

## 담당 파트
**정원준: 369게임**

**김규일: 숫자 맞추기 게임, intro** 

**이주원: 반응속도 게임**

**김은경: 랜덤 룰렛 게임** 

**이시은: 아파트**

## 진행
- **시작**: 01/04 16:30
- **1차 회의**: 01/06 00:00
- **2차 회의**: 01/06 22:00
- **마감**: 01/07 10:00

## 파일 구조

```
Piro22_PythonGame_5
  ├─setting
  │  ├─game_logic.py
  │  ├─party_setting.py
  │  └─text_asset.py
  ├─ games
  │  ├─1.py
  │  ├─UpDownGame.py
  │  ├─3.py
  │  ├─4.py
  │  └─5.py
  └─main.py
```
**main.py**

- 게임 시작점
- Player 정보 입력 및 게임 선택, 종료

### setting

**game_logic.py**

- **play_game:** 랜덤 게임 선택 상황에서 input 관리
- **except_input:** 그 외 input 상황에서 예외처리 관리

**party_setting.py**

- **initialize_party:** 파티 초기 설정
- **update_drink_status:** 현재 주량 출력
- **check_game_over:** gameover 메시지 출력

**text_assets.py**

- 프로그램 내에서 사용되는 text 관리

### games

**Updowngame.py**

- 업다운 게임
- 1~100 사이에 숫자가 정해져있다.
- 참가자는 돌아가면서 1~100 사이의 숫자를 말한다.
- 숫자를 말할 때마다 목표 숫자가 up인지 down인지 알 수 있다.
- 마지막에 숫자를 맞춘 사람의 전 사람이 술을 마신다.

## 참고
- [ASCII ART 생성](https://wepplication.github.io/tools/asciiArtGen/)
- [이모티콘 사용](https://www.emojiall.com/ko/categories/B)
