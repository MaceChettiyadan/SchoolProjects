import math
import random
from sympy import symbols, Eq, solve, solveset

machineDimensions = {"L": ["Le", "Lr", "Fr", "Fe"], "I": ["L", "h", "Fr"], "A": ["R", "r", "Fr", "Fe"],
                     "W": ["L", "t", "Fe"], "P": ["N", "Fr", "Fe"], "S": ["L", "P"]}


def calculateLever(dict):
    le = dict.get("Le")
    lr = dict.get("Lr")
    return le / lr


def calculateIncline(dict):
    l = dict.get("L")
    h = dict.get("h")
    return l / h


def calculateWheelAxle(dict):
    R = dict.get("R")
    r = dict.get("r")
    return R / r


def calculateWedge(dict):
    L = dict.get("L")
    t = dict.get("t")
    return L / t


def calculateScrew(dict):
    L = dict.get("L")
    P = dict.get("P")
    return (2 * math.pi * L)/P


def start():
    machineChoice = input("""Which machine would you like to use?:
                      Lever: L
                      Incline: I
                      Wheel and Axle: A
                      Wedge: W
                      Pulley: P
                      Screw: S
                      """)
    relativeDimensionsAsk = input("""Would you like to calculate relative dimensions?
    Yes: Y
    No: N
    """)
    if relativeDimensionsAsk.upper() == "N":
        setup(machineChoice)
    elif relativeDimensionsAsk.upper() == "Y":
        relativeDimensions(machineChoice)
    else:
        print('Input Invalid. Restarting')
        start()


def relativeDimensions(machineChoice):
    machineChoice = machineChoice.upper()
    try:
        forceInput = float(input("Enter force Input: "))
        forceOutput = float(input("Enter force Output: "))
        mechAdvantage = forceOutput/forceInput

        if machineChoice != "S" and machineChoice != "P":
            randomNumber = random.randint(1, 5)
            varOne = mechAdvantage*randomNumber
            varTwo = randomNumber
            print("""
            The Variable """ + machineDimensions.get(machineChoice.upper())[0] + """ is """ + str(varOne) + """.
            The Variable """ + machineDimensions.get(machineChoice.upper())[1] + """ is """ + str(varTwo) + """.
            """)
        if machineChoice == "P":
            print("""
            The Variable """ + machineDimensions.get(machineChoice.upper())[0] + """ is """ + str(mechAdvantage) + """.
            """)
        if machineChoice == "S":
            L, P = symbols('L P')
            sol = solveset(Eq((2 * math.pi * L)/P, mechAdvantage), L)
            sol2 = solveset(Eq((2 * math.pi * L) / P, mechAdvantage), P)
            lResult = str(sol.args[0]).split("*")[0]
            pResult = str(sol2.args[0]).split("*")[0].split("(")[1]
            print('The Variable L is ' + lResult + ' and the variable P is ' + pResult)

    except Exception as e:
        print(e)
        print('Input Invalid. Restarting')
        relativeDimensions(machineChoice)


def setup(machineChoice):
    tempDict = {}
    mechAdvantage = ""
    try:
        for varName in machineDimensions.get(machineChoice.upper()):
            tempDict[varName] = float(input("Please enter variable " + varName + "'s value: "))

    except:
        print('Input Invalid. Restarting')
        setup(machineChoice)
    if machineChoice.upper() == "L":
        mechAdvantage = str(calculateLever(tempDict))
    if machineChoice.upper() == "I":
        mechAdvantage = str(calculateIncline(tempDict))
    if machineChoice.upper() == "A":
        mechAdvantage = str(calculateWheelAxle(tempDict))
    if machineChoice.upper() == "W":
        mechAdvantage = str(calculateWedge(tempDict))
    if machineChoice.upper() == "P":
        mechAdvantage = str(tempDict.get("N"))
    if machineChoice.upper() == "S":
        mechAdvantage = str(calculateScrew(tempDict))

    print("Your Mechanical Advantage is " + mechAdvantage + " for this machine.")

    forceInputOutputCalc(mechAdvantage)


def forceInputOutputCalc(mechAdvantage):
    inOutchoice = input("""Would you like to calculate Force Input (for an output) or Force Output (for an input)?
        Output: O
        Input: I
        """)
    if inOutchoice.upper() == 'O':
        inputVar = float(input('Enter Input: '))
        print('Your force output is ' + str(inputVar * float(mechAdvantage)) + '.')
        return
    if inOutchoice.upper() == 'I':
        inputVar = float(input('Enter Output: '))
        print('Your force input required is ' + str(inputVar / float(mechAdvantage)) + '.')
        return
    else:
        print('Input Invalid. Restarting')
        forceInputOutputCalc(mechAdvantage)





start()
