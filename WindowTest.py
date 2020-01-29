import tkinter as tk
import tkinter.ttk as ttk

symbols = ["x", "y", "z"]

root = tk.Tk()
root.geometry("400x300")
root.title("積分オプション")

ImageOfIntegral = tk.PhotoImage(file = "image/integral.png")

canvas = tk.Canvas(width = 400, height = 300)
canvas.place(x = 0, y = 0)
canvas.create_image(100, 150, image = ImageOfIntegral)

discription = tk.Label(root, text = u"入力がなければ定積分を行います")
discription.pack()

a = tk.Entry(root, width = 3)
a.place(x = 120, y = 220)

b = tk.Entry(root, width = 3)
b.place(x = 180, y = 60)

selectTargetSymbol = tk.Label(root, text = u"について積分する")
selectTargetSymbol.place(x = 250, y = 140)

SymbolSelection = ttk.Combobox(root, state = "readonly", width = 3)
SymbolSelection["values"] = tuple(symbols)
SymbolSelection.current(0)
SymbolSelection.place(x = 200, y = 140)

def setOptions():
    pass

OkButton = tk.Button(root, text = "O K", command = setOptions)
OkButton.place(x = 300, y = 250)

root.mainloop()

