from guizero import App, Text, TextBox, PushButton, Window

#Funcao para verificação do login
def verificar_login(usuario, senha):
    with open('cadastros.txt', 'r+', encoding='utf-8') as cadastros:
        nomes = cadastros.readlines()
        for dados in nomes:
            linha = dados.strip().split(',')
            if len(linha) == 2 and linha[0] == usuario and linha[1] == senha:
                return True
    return False

#Funcao de login
def fazer_login():
    usuario_entrada = campo_user.value
    senha_entrada = campo_senha.value
    if verificar_login(usuario_entrada, senha_entrada):
        abrir_jan_principal()
        app.hide()
    else:
        print('ACESSO NEGADO')

#Funcao de verificar cadastro        
def cadastrar_usuario(username, password):
    with open('cadastros.txt', 'a', encoding='utf-8') as cadastros:
        cadastros.write(f"\n{username},{password}")
        

#Funcaao de cadastrar
def fazer_cadastro():
    user_cadastro = campo_user_cadastro.value
    senha_cadastro = campo_senha_cadastro.value

    if user_cadastro and senha_cadastro:
        cadastrar_usuario(user_cadastro, senha_cadastro)
        mostrar_cadastro()
    else:
        msg_cadastro.value = "Preencha todos os campos para cadastrar."

def mostrar_cadastro():
    janela_sucesso = Window(app, title='Sucesso!', width=200, height=100)
    Text(janela_sucesso, text="Cadastro realizado\ncom sucesso!")
    janela_sucesso.show()
    
    def fechar_janelas():
        janela_sucesso.hide()
        area_cadastro.hide()

    janela_sucesso._on_close = fechar_janelas
    janela_sucesso.show()
    
#Funcao de cancelar
def cancelar():
    print(f"Operação cancelada pelo usuário.")
    app.destroy()

#Funcao para janela de login admin
def abrir_jan_principal():
    msg_acesso.value = "ACESSO LIBERADO!"
    janela_principal.show()

#Funcao para janela de cadastro realizado
def janela_cadastro():
    area_cadastro.show()
    msg_cadastro.value = ''
    


#Inicializando o app
app = App(title="LOGIN", layout="grid", height=130, width=290)

#Janela principal para o admin
janela_principal = Window(app, title='ADMINISTRADOR', width=400, height=300)
janela_principal.hide()

#Area de login
msg_usuario = Text(app, text="Usuário: ",grid=[0,0])
campo_user = TextBox(app,grid=[1,0],width="fill")
msg_senha = Text(app, text="Senha: ",grid=[0,1])
campo_senha = TextBox(app,grid=[1,1],width="fill")
button_login = PushButton(app, text="Entrar", command=fazer_login,grid=[0,2])
button_cancel = PushButton(app, text="Cancelar", command=cancelar,grid=[1,2])
button_cadastrar = PushButton(app, text="Cadastrar", command=janela_cadastro, grid=[2,2])

#Janela Cadastro
area_cadastro = Window(app, title='CADASTRO', width=250, height=250)
msg_usuario_cadastro = Text(area_cadastro, text="Novo Usuário: ", grid=[0, 4])
campo_user_cadastro = TextBox(area_cadastro, grid=[1, 4], width="fill")
msg_senha_cadastro = Text(area_cadastro, text="Nova Senha: ", grid=[0, 5])
campo_senha_cadastro = TextBox(area_cadastro, grid=[1, 5], width="fill")
button_cadastro = PushButton(area_cadastro, text="Cadastrar", command=fazer_cadastro, grid=[0, 6])
msg_cadastro = Text(area_cadastro, text="", grid=[1,6])
area_cadastro.hide()

#Mensagem de acesso ao login admin
msg_acesso = Text(janela_principal, text="")
msg_cadastro = Text(area_cadastro, text="")

app.display()
