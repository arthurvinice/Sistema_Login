from guizero import App, Text, TextBox, PushButton, Window

#Funcao para verificar o login
def verificar_login(usuario, senha):
    with open('cadastros.txt', 'r+', encoding='utf-8') as cadastros:
        nomes = cadastros.readlines()
        for dados in nomes:
            linha = dados.strip().split(',')
            if len(linha) == 2 and linha[0] == usuario and linha[1] == senha:
                return True
    return False

#Funcaao de login
def fazer_login():
    usuario_entrada = campo_user.value
    senha_entrada = campo_senha.value
    if verificar_login(usuario_entrada, senha_entrada):
        abrir_jan_principal()
        app.hide()
    else:
        print('ACESSO NEGADO')

#Funcao de cancelar
def cancelar():
    print(f"Operação cancelada pelo usuário.")
    app.destroy()

#Funcao para fechar o app quando fechar a janela principal
def fechar_app():
    app.destroy()

#Funcao para apertar o enter
def press_enter(evento):
    if campo_user is not None and campo_senha is not None:
        if evento.key == '\r':
            fazer_login()
    else:
        print('ACESSO NEGADO')

#Funcao para segunda janela (apos login)
def abrir_jan_principal():
    msg_acesso.value = "ACESSO LIBERADO!"
    janela_principal.show()

#Inicializando o app
app = App(title="LOGIN", layout="grid", height=130, width=180)

#Janela principal para o admin
janela_principal = Window(app, title='ADMINISTRADOR', width=400, height=300)
janela_principal.hide()
janela_principal.when_closed = fechar_app

#Area de login
msg_usuario = Text(app, text="Usuário: ",grid=[0,0])
campo_user = TextBox(app,grid=[1,0],width="fill")
msg_senha = Text(app, text="Senha: ",grid=[0,1])
campo_senha = TextBox(app,grid=[1,1],width="fill")
campo_senha.when_key_pressed = press_enter
button_entrar = PushButton(app, text="Entrar",command=fazer_login,grid=[0,3])
Text(app, grid=[1,2])
button_cancelar = PushButton(app, text="Cancelar", command=cancelar,grid=[1,3])

#Mensagem de acesso ao login admin
msg_acesso = Text(janela_principal, text="")

app.display()
