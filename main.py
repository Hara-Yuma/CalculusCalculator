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
        message = tk.Toplevel()
        message.title("エラー")
        message.geometry("250x50")

        ErrorMessage = tk.Label(message, text = u"計算中にエラーが発生しました")
        ErrorMessage.pack()

        BackButton = tk.Button(message, text = "O K", command = message.destroy)
        BackButton.pack()

        message.mainloop()

    def differential():
        formula = cal.normalize(FormulaEntry.get())
        
        if formula == '':
            exception()

        symbols = cal.getSymbols(formula)

        if len(symbols) > 1:
            option = tk.Toplevel()
            option.title("微分オプション")
            option.geometry("250x100")

            selectTargetSymbol = tk.Label(option, ctext = u"について微分する")
            selectTargetSymbol.place(x = 120, y = 10)

            SymbolSelection = ttk.Combobox(option, state = "readonly", width = 3)
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
        formula = cal.normalize(FormulaEntry.get())

        if formula == '':
            exception()

        symbols = cal.getSymbols(formula)

        option = tk.Toplevel()
        option.title("積分オプション")
        option.geometry("400x300")
        
        ImageOfIntegral = tk.PhotoImage(file = "image/integral.png")

        canvas = tk.Canvas(option, width = 400, height = 300)
        canvas.place(x = 0, y = 0)
        canvas.create_image(100, 150, image = ImageOfIntegral)

        discription = tk.Label(option, text = u"入力がなければ定積分を行います")
        discription.pack()

        a = tk.Entry(option, width = 3)
        a.place(x = 120, y = 220)

        b = tk.Entry(option, width = 3)
        b.place(x = 180, y = 60)

        selectTargetSymbol = tk.Label(option, text = u"について積分する")
        selectTargetSymbol.place(x = 250, y = 140)

        SymbolSelection = ttk.Combobox(option, state = "readonly", width = 3)
        SymbolSelection["values"] = tuple(symbols)
        SymbolSelection.current(0)
        SymbolSelection.place(x = 200, y = 140)

        def execute():
            options = [SymbolSelection.get()]
            if (a.get() != '') and (b.get() != ''):
                options.append(float(a.get()))
                options.append(float(b.get()))

            cal.integral(
                    formula,
                    options,
                    result,
                    exception
                    )

        OkButton = tk.Button(option, text = "O K", command = execute)
        OkButton.place(x = 300, y = 250)

        option.mainloop()

    doDifferential = tk.Button(root, text = u"微分する", command = differential)
    doDifferential.place(x = 100, y = 100)
    doIntegral = tk.Button(root, text = u"積分する", command = integral)
    doIntegral.place(x = 220, y = 100)

    root.mainloop()

if __name__ == "__main__":
    calculator()

