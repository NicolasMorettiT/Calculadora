# importando Tkinter
from tkinter import *
from tkinter import ttk

# cores
cor1 = "#7b4abd" #roxo
cor2 = "#feffff" #branco
cor3 = "#38576b" #azul
cor4 = "#ECEFF1" #cinza
cor5 = "#3b3b3b" #preta


janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg= cor5)

# criando frames
frame_tela = Frame(janela, width=300, height=50, bg=cor3)
frame_tela.grid(row=0,column=0)

frame_corpo = Frame(janela, width=300, height=268)
frame_corpo.grid(row=1,column=0)

#criando labels

valor_texto = StringVar()
app_Label = Label(frame_tela, textvariable=valor_texto, width="17", height="2", padx=7, relief=FLAT, anchor="e", justify=RIGHT, font="Ivy 17", bg= cor3, fg=cor2)
app_Label.place(x=0,y=0)

# variavel todos valores
todos_valores = ''

#criando funcao
def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    #passando o valor para o Label
    valor_texto.set(todos_valores)
    
 
#funcao para calcular 
def calcular():
    global todos_valores
    try:
        resultado = eval(todos_valores)
        valor_texto.set(str(resultado))
    except Exception as e:
        valorTexto.set('Erro')
        todosValores = ""
    
    # funcao limpar tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")
#criando botoes

b_C = Button(frame_corpo, command= limpar_tela ,text="C", width="11", height="2", bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_C.place(x=0,y=0)
b_Mod = Button(frame_corpo, command= lambda: entrar_valores('%'), text="%", width="5", height="2", bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_Mod.place(x=120,y=0)
b_D = Button(frame_corpo, command= lambda: entrar_valores('/'),text="÷", width="5", height="2", bg=cor1, fg=cor2, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE, )
b_D.place(x=180,y=0)

b_7 = Button(frame_corpo, command= lambda: entrar_valores('7'),text="7", width="5", height="2", bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_7.place(x=0,y=52)
b_8 = Button(frame_corpo, command= lambda: entrar_valores('8'),text="8", width="5", height="2", bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_8.place(x=60,y=52)
b_9 = Button(frame_corpo, command= lambda: entrar_valores('9'),text="9", width="5", height="2", bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_9.place(x=120,y=52)
b_X = Button(frame_corpo, command= lambda: entrar_valores('*'),text="×", width="5", height="2", bg=cor1, fg=cor2, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_X.place(x=180,y=52)

b_4 = Button(frame_corpo, command= lambda: entrar_valores('4'),text="4", width="5", height="2", bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_4.place(x=0,y=104)
b_5 = Button(frame_corpo, command= lambda: entrar_valores('5'),text="5", width="5", height="2", bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_5.place(x=60,y=104)
b_6 = Button(frame_corpo, command= lambda: entrar_valores('6'),text="6", width="5", height="2", bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_6.place(x=120,y=104)
b_M = Button(frame_corpo, command= lambda: entrar_valores('-'),text="-", width="5", height="2", bg=cor1, fg=cor2, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_M.place(x=180,y=104)

b_1 = Button(frame_corpo, command= lambda: entrar_valores('1'),text="1", width="5", height="2", bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_1.place(x=0,y=156)
b_2 = Button(frame_corpo, command= lambda: entrar_valores('2'),text="2", width="5", height="2", bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_2.place(x=60,y=156)
b_3 = Button(frame_corpo, command= lambda: entrar_valores('3'),text="3", width="5", height="2", bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_3.place(x=120,y=156)
b_S = Button(frame_corpo, command= lambda: entrar_valores('+'),text="+", width="5", height="2", bg=cor1, fg=cor2, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_S.place(x=180,y=156)

b_0 = Button(frame_corpo, command= lambda: entrar_valores('0'),text="0", width="11", height="2", bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_0.place(x=0,y=208)
b_P = Button(frame_corpo, command= lambda: entrar_valores('.'),text=".", width="5", height="2", bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_P.place(x=120,y=208)
b_I = Button(frame_corpo, command = calcular, text="=", width="5", height="2", bg=cor1, fg=cor2, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_I.place(x=180,y=208)

janela.mainloop()