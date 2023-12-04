from guizero import App, Text, TextBox, PushButton, Window

#Funcao para login
def fazer_login():
    with open('cadastros.txt', 'r+', encoding='utf-8') as cadastros:
        nomes = cadastros.readlines()
        for linha in nomes:
            user, senha = linha.strip().split(',')
            if user == campo_user.value and senha == campo_senha.value:
                abrir_jan_principal()
                app.hide()
    print("ACESSO NEGADO!")
        

#Funcao de cancelar
def cancelar():
    print(f"Operação cancelada pelo usuário.")
    app.destroy()

#Funcao para segunda janela
def abrir_jan_principal():
    msg_acesso.value = "ACESSO LIBERADO!"
    janela_principal.show()

#Inicializando o app
app = App(title="LOGIN", layout="grid", height=130, width=180)

#Janela principal para o admin
janela_principal = Window(app, title='ADMINISTRADOR', width=400, height=300)
janela_principal.hide()

#Area de login
msg_usuario = Text(app, text="Usuário: ",grid=[0,0])
campo_user = TextBox(app,grid=[1,0],width="fill")
msg_senha = Text(app, text="Senha: ",grid=[0,1])
campo_senha = TextBox(app,grid=[1,1],width="fill")
button = PushButton(app, text="Entrar", command=fazer_login,grid=[0,3])
Text(app, grid=[1,2])
button = PushButton(app, text="Cancelar", command=cancelar,grid=[1,3])

#Mensagem de acesso ao login admin
msg_acesso = Text(janela_principal, text="")

app.display()