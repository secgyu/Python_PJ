# doWelcome = print 여러 개 이용해 게임소개 및 현재 플레이어 위치 알려줌
# doStart = 게임 시작 장소를 정의한 함수, 텍스트와 함께 사용자의 선택을 기다리는 프롬프트 표시하고 선택에 따라 해당하는 장소로 이동
# doBoulders = 장소 : 바위더미
# doStructure = 장소 : 구조물
# doStructureDoor = 장소 : 구조물 입구
# doBeeping = 삐 소리 탐색
# doRun = 도망


import Strings
import Utils


def doWelcome():
    print(Strings.get("Welcome"))


def doStart():
    print(Strings.get("Start"))
    choices = [
        ["P", "바위 더미를 조사한다"],
        ["S", "구조물에 접근한다"],
        ["B", "삐 소리가 나는 곳으로 간다"],
        ["R", "도망간다!"]
    ]
    choice = Utils.getUserChoice(choices)
    if choice == 'P':
        doBoulders()
    elif choice == 'S':
        doStructure()
    elif choice == 'B':
        doBeeping()
    elif choice == 'R':
        doRun()


def doBoulders():
    print(Strings.get("Boulders"))
    doStart()


def doStructure():
    print(Strings.get("Structure"))
    choices = [
        ["S", "시작 지점으로 돌아간다"],
        ["D", "문을 연다"],
        ["B", "삐 소리가 나는 곳으로 간다"],
        ["R", "도망간다!"]
    ]
    choice = Utils.getUserChoice(choices)
    if choice == 'S':
        doStart()
    elif choice == 'D':
        doStructureDoor()
    elif choice == 'B':
        doBeeping()
    elif choice == 'R':
        doRun()


def doStructureDoor():
    print(Strings.get("StructureDoor"))
    print(Strings.get("StructureDoorNoKey"))
    choices = [
        ["S", "구조물로 돌아간다"],
        ["R", "도망간다!"]
    ]
    choice = Utils.getUserChoice(choices)
    if choice == 'S':
        doStructure()
    elif choice == 'R':
        doRun()


def doBeeping():
    pass


def doRun():
    print(Strings.get("Run"))
    gameOver()


def gameOver():
    print(Strings.get("GameOver"))


doWelcome()
# 게임 시작하기
doStart()
