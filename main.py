import tkinter as tk
import tkinter.ttk as ttk
import calculation as cal

def calculator():
    root = tk.Tk()
    root.title(u"微積分計算機")
    root.geometry("400x150")
    root.resizable(0, 0)

    enterFormula = tk.Label(root, text = u"数式を入力: ")
    enterFormula.place(x = 20, y = 30)

    FormulaEntry = tk.Entry(root, width = 30)
    FormulaEntry.place(x = 120, y = 30)

    def result(answer):
        cal.showAnswer(str(answer))

    def exception():
        # 計算時のエラーが発生した際に実行する処理
        pass

    def differential():
        formula = cal.normalize(FormulaEntry.get())
        symbols = cal.getSymbols(formula)

        if len(symbols) > 1:
            option = tk.Toplevel()
            option.title("微分オプション")
            option.geometry("250x100")

            selectTargetSymbol = tk.Label(option, text = u"について微分する")
            selectTargetSymbol.place(x = 120, y = 10)

            SymbolSelection = ttk.Combobox(option, state="readonly", width = 3)
            SymbolSelection["values"] = tuple(symbols)
            SymbolSelection.current(0)
            SymbolSelection.place(x = 70, y = 10)
            
            def setTargetSymbol():
                TargetSymbol = SymbolSelection.get()
                option.destroy()
                cal.differential(
                        formula,
                        TargetSymbol,
                        result,
                        exception)

            OkButton = tk.Button(option, text = "O K", command = setTargetSymbol)
            OkButton.place(x = 120, y = 50)
            option.mainloop()
        else:
            cal.differential(
                    formula,
                    '',
                    result,
                    exception)

    def integral():
        # 積分選択時の処理
        return

    doDifferential = tk.Button(root, text = u"微分する", command = differential)
    doDifferential.place(x = 100, y = 100)
    doIntegral = tk.Button(root, text = u"積分する", command = integral)
    doIntegral.place(x = 220, y = 100)

    root.mainloop()

if __name__ == "__main__":
    calculator()

