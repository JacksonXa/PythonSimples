import tkinter as tk

# 1 Criando a Janela
window = tk.Tk()
window.geometry("300x150")
window.title("Gerencia Frases")

# 2 - Adiciona um Frame
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill='x', expand=True)

# 3 - Adcionando o Label
label = tk.Label(frame, text="Hey my friend!")
label.pack(fill='x', expand=True)

# 4 - Adicionando o input text
frase_lab = tk.Label(frame, text="Frase")
frase_lab.pack(fill='x', expand=True)

frase_inp = tk.Entry(frame)
frase_inp.pack(fill='x', expand=True)

# 5 - Funcao para alterar o texto do label
"""Ao clicar no botao, devera mudar a frase"""
def click():
    label.config(text=frase_inp.get())

# 6 - Adicionando o Botao
button = tk.Button(frame, text="Enviar", command=click)
button.pack()

window.mainloop()