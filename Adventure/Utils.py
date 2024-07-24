# 유틸리티 함수

def getUserChoice(options):
    validInputs = ""
    for opt in options:
        validInputs += opt[0]
        print(opt[0], "-", opt[1])
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
