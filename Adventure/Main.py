import Strings
import Utils
import Inventory as inv
import Player
import random
import Enemies
from colorama import init, Fore

p = Player.player()

init()


def doWelcome():
    print(Fore.GREEN + Strings.get("Welcome"))


def doStart():
    print(Strings.get("Start"))
    choices = [
        ["P", "바위 더미를 조사한다"],
        ["S", "구조물에 접근한다"],
        ["B", "삐 소리가 나는 곳으로 간다"],
        ["R", "도망간다!"],
        ["I", "인벤토리"],
        ["C", "전투"],
        ["T", "상점"],
        ["E", "탐험 (무작위 이벤트)"]
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
    elif choice == "I":
        inv.display()
        doStart()
    elif choice == 'C':
        doCombat()
    elif choice == 'T':
        doStore()
    elif choice == 'E':
        randomEvent()


def doBoulders():
    p.visitBoulder()
    if p.getBoulderVisits() == 1:
        print(Strings.get("Boulders"))
    elif p.getBoulderVisits() == 3:
        print(Strings.get("BouldersKey"))
        inv.takeStructureKey()
    else:
        print(Strings.get("Boulders2"))
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
    print(Fore.GREEN + Strings.get("StructureDoor"))
    if inv.hasStructureKey():
        print(Fore.GREEN + Strings.get("StructureDoorKey"))
    else:
        print(Fore.RED + Strings.get("StructureDoorNoKey"))
    choices = [
        ["S", "구조물로 돌아간다"],
        ["R", "도망간다!"]
    ]
    if inv.hasStructureKey():
        choices.insert(0, ["U", "열쇠로 문을 연다"])
    choice = Utils.getUserChoice(choices)
    if choice == 'S':
        doStructure()
    elif choice == 'R':
        doRun()
    elif choice == 'U':
        doEnterStructure()


def doBeeping():
    pass


def doEnterStructure():
    pass


def doRun():
    print(Fore.GREEN + Strings.get("Run"))
    p.died()
    if p.isAlive():
        doStart()
    else:
        gameOver()


def gameOver():
    print(Fore.GREEN + Strings.get("GameOver"))
    if Utils.inputYesNo("다시 시작하시겠습니까?"):
        p.addLife(3)
        p.addHealth(p.maxHealth)
        inv.dropCoins(inv.numCoins())
        doStart()
    else:
        print("게임을 종료합니다.")


def doCombat():
    enemy = Enemies.getEnemy(random.choice(["slug", "eel", "alien"]))
    print(f"적이 나타났습니다: {enemy['description']} (체력: {enemy['strength']})")
    while enemy["strength"] > 0 and p.isAlive():
        choice = input("공격[A] / 도망[R]: ").upper()
        if choice == "A":
            damage_to_enemy = p.attackEnemy(enemy)
            damage_to_player = p.attack(random.randint(
                enemy["damageMin"], enemy["damageMax"]))
            print(f"{enemy['description']}에게 {damage_to_enemy}의 피해를 입혔습니다!")
            print(f"{enemy['description']}에게 {damage_to_player}의 피해를 입었습니다!")
            if p.getHealth() <= 0:
                print("당신은 패배했습니다!")
                p.died()
                break
            if enemy["strength"] <= 0:
                print("적을 물리쳤습니다!")
                break
        elif choice == "R":
            print("도망쳤습니다!")
            break

    if not p.isAlive():
        gameOver()
    else:
        doStart()


def randomEvent():
    if Utils.randomEvent(4):
        print("길에서 동전 100개를 발견했습니다.")
        print("동전을 줍습니다.")
        inv.takeCoins(100)
    else:
        events = ["C", "P", "S"]
        event = random.choice(events)
        if event == "C":
            doCombat()
        elif event == "P":
            doBoulders()
        elif event == "S":
            doStructure()


def doStore():
    print("상점에 오신 것을 환영합니다!")
    Utils.buyItem()
    doStart()


doWelcome()
doStart()
