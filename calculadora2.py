import tkinter as tk

def instxt(num):
    texto.insert(1.0,num)

janela = tk.Tk()
janela.geometry("420x520")

texto=tk.Text(janela,height=2, width=6, font=("arial", 36))
texto.grid(columnspan=4)

botao1=tk.Button(janela, text="1", command=lambda:instxt("1"), height=2, width=4, font=("arial", 36))
botao1.grid(column=1, row=2)

janela.mainloop()