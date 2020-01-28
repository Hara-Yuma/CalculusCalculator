import tkinter as tk
import sympy as sp

numbers = "0 1 2 3 4 5 6 7 8 9".split()
OperatorSymbols = "+ - * / ^".split()
blank = [' ']

def isSymbol(c):
    return (c not in (numbers + OperatorSymbols + blank))

def normalize(FormulaString):
    if len(FormulaString) == 0:
        return ""
    normalized = FormulaString[0]
    for i in range(len(FormulaString) - 1):
        if (FormulaString[i] not in OperatorSymbols + blank) and (isSymbol(FormulaString[i + 1])):
            normalized = normalized + '*'
        elif FormulaString[i + 1] == '^':
            normalized = normalized + "**"
            continue
        normalized = normalized + FormulaString[i + 1]
    return normalized

def getSymbols(FormulaString):
    Symbols = []
    for c in FormulaString:
        if isSymbol(c):
            Symbols.append(c)
    return set(Symbols)

def differential(FormulaString, TargetSymbol, result, exception):
    try:
        if TargetSymbol == '':
            result(sp.diff(FormulaString))
        else:
            result(sp.diff(FormulaString, TargetSymbol))
    except:
        exception()

def showAnswer(answer):
    result = tk.Toplevel()
    result.title(u"計算結果")
    result.geometry("250x50")

    showed = ""
    for i in range(len(answer)):
        if answer[i] != '*':
            showed = showed + answer[i]
        elif answer[i + 1] == '*':
            showed = showed + '^'

    formula = tk.Label(result, text = showed)
    formula.pack()

    OkButton = tk.Button(result, text = "O K", command = result.destroy)
    OkButton.pack()

    result.mainloop()

