import tkinter as tk
import webbrowser

def linkedin(event):
    webbrowser.open_new_tab('https://www.linkedin.com/in/heber-levy-almeida-61b209140/')

def github(event):
    webbrowser.open_new_tab('https://github.com/Heber3000')



janela = tk.Tk()
janela.title('App')
janela.geometry("300x200")
labell = tk.Label(text="Minhas Mídias:")
labell.grid(column=0,row=0)


botao1 = tk.Button(janela,text='Linkedin',bg='red')
botao1.grid(column=1,row=1)
botao2 = tk.Button(janela,text='Github', bg='green')
botao2.grid(column=3,row=1)

botao1.bind("<Button-1>", linkedin)
botao2.bind("<Button-1>", github)





janela.mainloop()
