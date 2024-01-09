from Login import usuario, senha

class Usuario():
    def __init__(self, codigo, nome=usuario.value, senha=senha.value):
        self.codigo = codigo
        self.nome = nome
        self.senha = senha
