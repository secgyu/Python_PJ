# 인벤토리 시스템

inv = {
    "StructureKey": False,
    "Coins": 0,
    "LaserBlaster": False,
    "QuantumGrenades": 0,
    "PlasmaShield": False,
    "GalacticMap": False,
}


def takeStructureKey():
    inv["StructureKey"] = True


def dropStructureKey():
    inv["StructureKey"] = False


def hasStructureKey():
    return inv["StructureKey"]


def takeCoins(coins):
    inv["Coins"] += coins


def dropCoins(coins):
    inv["Coins"] -= coins


def numCoins():
    return inv["Coins"]


def takeLaserBlaster():
    inv["LaserBlaster"] = True


def dropLaserBlaster():
    inv["LaserBlaster"] = False


def hasLaserBlaster():
    return inv["LaserBlaster"]


def takeGrenades(grenades):
    inv["QuantumGrenades"] += grenades


def dropGrenades(grenades):
    inv["QuantumGrenades"] -= grenades


def numGrenades():
    return inv["QuantumGrenades"]


def takePlasmaShield():
    inv["PlasmaShield"] = True


def dropPlasmaShield():
    inv["PlasmaShield"] = False


def hasPlasmaShield():
    return inv["PlasmaShield"]


def takeGalacticMap():
    inv["GalacticMap"] = True


def dropGalacticMap():
    inv["GalacticMap"] = False


def hasGalacticMap():
    return inv["GalacticMap"]


def display():
    print("******* 인벤토리 *******")
    print("가진 동전은 ", numCoins(), "개입니다.")
    if hasStructureKey():
        print("파랗게 빛나는 열쇠가 있습니다.")
    if hasGalacticMap():
        print("은하계 지도가 있습니다.")
    if hasPlasmaShield():
        print("플라스마 방패가 있습니다.")
    if hasLaserBlaster() == False and numGrenades() == 0:
        print("아무런 무기도 없습니다.")
    if hasLaserBlaster():
        print("광선총이 있습니다.")
    if numGrenades() > 0:
        print(numGrenades(), "개의 퀀텀 수류탄이 있습니다.")
    print("************************")
