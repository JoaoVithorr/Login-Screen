from tkinter import *
from tkinter import ttk, Tk
from tkinter import messagebox

# Cores:
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#3fb5a3"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra

# Criando a janela:
root = Tk () # janela criada
root.title("")
root.geometry("310x300") # Tamanho da janela definido 
root.configure(background= co1) # Colocando um fundo branco na root


# Frames: Dividindo a janela em duas partes: cima e baixo
frame_upper = Frame(root, width= 310, height=50, bg= co1, relief= "flat") # Definindo medidas, cores de fundo e linhas.
frame_upper.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
frame_lower = Frame(root, width= 310, height= 300, bg= co1, relief= "flat")
frame_lower.grid(row=1, column=0,pady=1, padx=0, sticky=NSEW)

# Criando alguns rótulos e entrada dentro do frame superior que definirão o nome do app e também uma linha para estilizar a tela.
l_titulo = Label(frame_upper, text= "LOGIN", height=1, anchor=NE, font=("Ivy 25"), bg=co1, fg=co4)
l_titulo.place(x=5, y=5)


l_linha = Label(frame_upper,width=275, text="", height=1,anchor=NW, font=('Ivy 1 '), bg=co2)
l_linha.place(x=10, y=45)

# Criando rótulos e entradas para o frame inferior, onde o usuário pode inserir nome e senha, assim como o botão de confirmar.
l_name = Label(frame_lower, text="Name *", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_name.place(x=10, y=20)
e_name = Entry(frame_lower, width=25, justify='left',font=("",15),highlightthickness=1, relief="solid")
e_name.place(x=14, y=50)

l_pass = Label(frame_lower, text="Password *", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_pass.place(x=10, y=95)
e_pass = Entry(frame_lower,show='*',width=25, justify='left',font=("",15),highlightthickness=1,relief="solid")
e_pass.place(x=15, y=130)

button_confirm = Button(frame_lower, text="Login", width=39, height=2, bg=co2, fg=co1, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
button_confirm.place(x=15, y=180)

# Criando credenciais para acesso:
credenciais = ["admin", "admin"]

# Função que contém a lógica do programa:
def verify():
    name_ = e_name.get() # Pega o nome da entrada do usuário
    pswd_ = str(e_pass.get())

    if name_ == "admin" and pswd_ == "admin":
        messagebox.showinfo("Login", "Welcome, Adm!")

     # verificando os dados para permitir o login do usuario
    elif credenciais[0] == name_ and credenciais[1] == pswd_:
        messagebox.showinfo('Login',' Welcome back! '+credenciais[0])

        # apagar o que tiver no frame baixo e cima
        for widget in frame_baixo.winfo_children():
            widget.destroy()
        
        for widget in frame_cima.winfo_children():
            widget.destroy()

            # Chamar nova root
            new_window()
            
    else:
        messagebox.showwarning('Error', 'Verify your name and password.')

button_confirm = Button(frame_lower, command= verify, text="Login", width=39, height=2, bg=co2, fg=co1, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
button_confirm.place(x=15, y=180)

def new_window():
    l_name = Label(frame_upper, text="User: " + credenciais[0], height=1,anchor=NE, font=('Ivy 20 '), bg=co1, fg=co4)
    l_name.place(x=5, y=5)

    l_line = Label(frame_upper,width=275, text="", height=1,anchor=NW, font=('Ivy 1 '), bg=co2)
    l_line.place(x=10, y=45)
    
    l_name = Label(frame_lower, text="Welcome " + credenciais[0], height=1,anchor=NE, font=('Ivy 15 '), bg=co1, fg=co4)
    l_name.place(x=5, y=105)

root.mainloop()