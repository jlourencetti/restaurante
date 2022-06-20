from turtle import title


class Usuario():

    def __init__(self, primeiro_nome, segundo_nome):
        self.primeiro_nome = primeiro_nome
        self.segundo_nome = segundo_nome
        
    def perfil_usuario(idade, user_name):
        pass

    def descrição_usuario(self):
        print(f"Os dados do usuário são: {self.primeiro_nome.title()} {self.segundo_nome.title()}")

    def cumprimentar_usuario(self):
        print(f"Ficamos muito felizes de ve-lo por aqui {self.primeiro_nome.title()}")

usuario_1 = Usuario("Juliano", "Lourencetti")
print(usuario_1.primeiro_nome.title(), usuario_1.segundo_nome.title())

usuario_1.descrição_usuario()
usuario_1.cumprimentar_usuario()
