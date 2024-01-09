from guizero import Window, PushButton, Text, Picture, error, info


def fechar_app(app):
    return app.destroy()
def voltar_app(janela_acesso_ok):
    return janela_acesso_ok.destroy()

def verificar_usuario(usuario, senha, codigo, app):
    usuario_existente = False
    codigo_existente = False
    
    with open("arquivo.txt", "r") as dados:
        for linha in dados:
            partes = linha.split(",")
            if len(partes) == 3 and usuario.value == partes[0].strip():
                usuario_existente = True
                break

    with open("arquivo.txt", "r") as dados:
        for linha in dados:
            partes = linha.split(",")
            if len(partes) == 3 and codigo.value == partes[2].strip():
                codigo_existente = True
                break

    if usuario_existente:
        print("Usuário existente")
        error(title="ERRO", text=f"Este Usuário já existe!\nTente um diferente." )
    elif codigo_existente:
        error(title="ERRO", text=f"Este código já existe!\nTente um diferente." )
        print("Código existente")
    else:
        cadastrar_usuario(usuario, senha, codigo, app)

def cadastrar_usuario(usuario, senha, codigo, app):

    with open("arquivo.txt", "a") as dados:
        dados.write(f"{usuario.value},{senha.value},{codigo.value}")
        dados.write("\n")
    

    info("Cadastro finalizado!","Cadastro realizado com sucesso")

def login(usuario, senha, codigo, app):
    logado = False
    with open("arquivo.txt", 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            partes = linha.split(",")
            if len(partes) == 3 and usuario.value != partes[0].strip() and senha.value == partes[1].strip() and codigo.value == partes[2].strip():
                error(title='ERRO', text="Usuário incorreto ou campo vazio!")
                logado = False
                break
            elif len(partes) == 3 and usuario.value == partes[0].strip() and senha.value != partes[1].strip() and codigo.value == partes[2].strip():
                error(title='ERRO', text="Senha incorreta ou campo vazio!")
                logado = False
                break
            elif len(partes) == 3 and usuario.value == partes[0].strip() and senha.value == partes[1].strip() and codigo.value != partes[2].strip():
                error(title='ERRO', text="Código incorreto ou campo vazio!")
                logado = False
                break
            else:
                logado = True
                
    if logado:
        janela_acesso_ok = Window(app, title='TELA PRINCIPAL', width=460, height=400, layout='grid')
        text_nada = Text(janela_acesso_ok, text="", grid=[0,0])
        msg_acesso_ok = Text(janela_acesso_ok, text="ACESSO AUTORIZADO", grid=[1,0])
        msg_acesso_ok.text_size = 16
        text_nada = Text(janela_acesso_ok, text="", grid=[0,2], width=10)
        text_nada2 = Text(janela_acesso_ok, text="", grid=[1,2], height=5)
        btn_fechar = PushButton(janela_acesso_ok, text='FECHAR APLICATIVO', command=lambda: fechar_app(app), grid=[1,3])
        btn_fechar.tk.config(cursor='hand2')
       
        text_nada3 = Text(janela_acesso_ok, text="", grid=[1,4], height=1)

        btn_voltar = PushButton(janela_acesso_ok, text='VOLTAR AO INÍCIO', command=lambda: voltar_app(janela_acesso_ok), grid=[1,5])
        btn_voltar.tk.config(cursor='hand2')
        
        
        img = Picture(janela_acesso_ok, image="comu.png", grid=[1,1])
        
        janela_acesso_ok.bg = "#2C3E50"
        janela_acesso_ok.text_color = "white"
        janela_acesso_ok.font = "Arial"
        janela_acesso_ok.text_size = 14
        janela_acesso_ok.show(wait=True)
        janela_acesso_ok.tk.resizable(False, False)
        

def buscar_usuario(valor,app):
    existe = False
    cod_user_procurado = None
    user_cod_procurado = None

    with open("arquivo.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            partes = linha.split(",")
            if len(partes) == 3:
                if partes[0].strip() == valor:
                    cod_user_procurado = partes[2].strip()
                    
                    info("Usuário encontrado!",f"Usuário: {valor}\nCódigo: {cod_user_procurado}")

                    print(f"Usuário encontrado!\nUsuário: {valor}\nCódigo: {cod_user_procurado}")
                    existe = True
                    break
                
                if partes[2].strip() == valor:
                    user_cod_procurado = partes[0].strip()

                    info("Código encontrado!",f"Usuário: {user_cod_procurado}\nCódigo: {valor}")

                    print(f"Código encontrado!\nUsuário: {user_cod_procurado}\nCódigo: {valor}")
                    existe = True
                    break
    if not existe:
        error(title='ERRO', text="Usuário ou Código não encontrado!")

def excluir_usuario(codigo,app):
    with open("arquivo.txt", 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
    
    with open("arquivo.txt", "w", encoding='utf-8') as arquivo:
        user_excluido = ''
        cod_excluido = ''

        for linha in linhas:
            partes = linha.strip().split(',')
            if len(partes) >= 3 and partes[2].strip() == str(codigo):
                user_excluido = partes[0].strip()
                cod_excluido = partes[2].strip()
            else:
                arquivo.write(linha)
    
        if user_excluido and cod_excluido:

            info("Usuário excluído.",f"Usuário: {user_excluido}\nCódigo: {cod_excluido}")

        else:
            error(title="ERRO", text=f"Código de usuário {codigo} não encontrado!")

