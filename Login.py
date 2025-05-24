from guizero import App, Text, TextBox, PushButton
from Persistencia import verificar_usuario, buscar_usuario, excluir_usuario, login

#Limpar campos
def limpar_campos():
    usuario.clear()
    senha.clear()
    codigo.clear()
    input_busca.clear()
    input_excluir.clear()

# Tela de Principal
app = App(title="Tela de Login", layout='grid', width=410, height=540)
app.bg = "#2C3E50"
app.text_color = "white"
app.font = "Arial"
app.text_size = 12

# Inputs
# Input (usuário)
texto_usuario = Text(app, text="Usuário: ", grid=[1,0])
texto_usuario.text_size = 14
usuario = TextBox(app, width=15, grid=[2,0])
usuario.bg = "white"
usuario.text_color = "black"

# Input (senha)
texto_senha = Text(app, text="Senha: ", grid=[1,1])
texto_senha.text_size = 14
senha = TextBox(app, width=15, grid=[2,1], hide_text=True)
senha.bg = "white"
senha.text_color = "black"

# Input (codigo)
texto_codigo = Text(app, text="Código: ", grid=[1,2])
texto_codigo.text_size = 14
codigo = TextBox(app, width=15, grid=[2,2])
codigo.bg = "white"
codigo.text_color = "black"

text_nada = Text(app, text="", grid=[0,3], width=0)
text_nada2 = Text(app, text="", grid=[1,3], width=0)

#Botões (LOGAR, CADASTRAR E CANCELAR)
btn_login = PushButton(app, text="Login", width=7, command=lambda: login(usuario, senha, codigo, app), grid=[2,4])
btn_login.text_color = 'white'
btn_login.bg = '#6ca0dc'
btn_login.tk.config(cursor='hand2')

text_nada3 = Text(app, text="", grid=[2,5] , height=1)

btn_cadastrar = PushButton(app, text="Cadastrar", width=7, command=lambda: verificar_usuario(usuario, senha, codigo, app), grid=[2,6])
btn_cadastrar.bg = '#6ca0dc'
btn_cadastrar.text_color = 'white'
btn_cadastrar.tk.config(cursor='hand2')

text_nada4 = Text(app, text="", grid=[2,7], height=1)

btn_cancelar = PushButton(app, text="Cancelar", width=7, command=app.destroy, grid=[2,8])
btn_cancelar.text_color = 'white'
btn_cancelar.bg = '#E74C3C'
btn_cancelar.tk.config(cursor='hand2')

text_nada5 = Text(app, text="", grid=[2,9], height=1)

#Parte de Busca
text_busca = Text(app, text="Buscar usuário: ", grid=[1,10])
text_busca.text_size = 14
input_busca = TextBox(app, width=12, grid=[2,10])
input_busca.bg = "white"
input_busca.text_color = "black"

text_nada6 = Text(app, text="", grid=[3,10], width=1, height=1)

btn_buscar = PushButton(app, command=lambda: buscar_usuario(input_busca.value, app), image="lupa.png", grid=[4,10]) 
btn_buscar.bg = '#d3c1af'
btn_buscar.tk.config(cursor='hand2')

text_nada7 = Text(app, text="", grid=[3,11], width=1, height=1)
text_nada8 = Text(app, text="", grid=[4,11], width=1, height=1)

#Parte de Exclusão
text_excluir = Text(app, text="Excluir usuário: ", grid=[1,12])
text_excluir.text_size = 14
input_excluir = TextBox(app, width=12, grid=[2,12])
input_excluir.bg = "white"
input_excluir.text_color = "black"

btn_excluir = PushButton(app, image="excluir.png", command=lambda: excluir_usuario(input_excluir.value, app), grid=[4,12])
btn_excluir.bg = "#E74C3C"  
btn_excluir.text_color = "white"
btn_excluir.tk.config(cursor='hand2')

text_nada9 = Text(app, text="", grid=[2,13], width=1, height=1)

#Limpar os campos
btn_limpar_tudo = PushButton(app, text="LIMPAR \nCAMPOS", command=limpar_campos, grid=[2,14], width=12, height=1)
btn_limpar_tudo.bg = "#3e3e3e"
btn_limpar_tudo.text_color = "white"
btn_limpar_tudo.tk.config(cursor='hand2')

#Impedir o redimensionamento
app.tk.resizable(False, False)
app.display()
