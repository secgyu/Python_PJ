import random
import Inventory as inv
import Player as p
from Items import items
from colorama import Fore


def getUserChoice(options):
    validInputs = ""
    for opt in options:
        validInputs += opt[0]
        print(Fore.YELLOW + opt[0], "-", opt[1])
    prompt = "무엇을 하고 싶으세요? [" + validInputs + "]: "
    choice = ""
    done = False
    while not done:
        choice = input(prompt).strip().upper()
        if len(choice) > 1:
            choice = choice[0]
        if len(choice) == 1 and choice in validInputs:
            done = True
    return choice


def inputNumber(prompt):
    inp = ""
    while not inp.isnumeric():
        inp = input(prompt).strip()
    return int(inp)


def inputYesNo(text):
    while True:
        x = input(text + " [Y/N]").upper()
        if x in ["Y", "YES"]:
            return True
        elif x in ["N", "NO"]:
            return False


def getItems():
    result = []
    for item in items:
        i = []
        i.append(item["key"])
        i.append(item["description"] + " (" + str(item["cost"]) + ")")
        result.append(i)
    return result


def randomEvent(freq):
    return True if random.randrange(0, freq) == 0 else False


def buyItem():
    items_for_sale = getItems()
    for item in items_for_sale:
        print(f"{item[0]}: {item[1]}")
    choice = input("구매할 아이템을 선택하세요: ").upper()
    for item in items:
        if item["key"] == choice:
            if inv.numCoins() >= item["cost"]:
                inv.takeCoins(item["cost"])
                if choice == "H":
                    p.addHealth(50)
                elif choice == "B":
                    inv.takeLaserBlaster()
                elif choice == "G":
                    inv.takeGrenades(3)
                elif choice == "S":
                    inv.takePlasmaShield()
                elif choice == "L":
                    p.addLife()
                print(f"{item['description']}을(를) 구매했습니다!")
            else:
                print("동전이 부족합니다!")
            break
