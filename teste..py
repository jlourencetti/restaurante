class Restaurante():

    def __init__(self, name, tipo_cozinha ):
        self.name = name
        self.tipo_cozinha = tipo_cozinha
        self.pessoas_atendidas = 0

    def descrever_restaurante(self):
        print(f"Esse restaurante se chama {self.name} e é {self.tipo_cozinha} ")

    def restaurante_aberto(self):
        print(f"O restaurante {self.name} com cozinha {self.tipo_cozinha} esta aberto!")

    def atendimentos(self):
        print(f"O numero de pessoas atendidas foi: {self.pessoas_atendidas}")

    def pessoas_servidas(self, quantidade):
        self.pessoas_atendidas = quantidade

    def incrementa_servidos(self, quantidade):
        self.pessoas_atendidas += quantidade



restaurante = Restaurante('Guilere', 'Italiano')
print(f"O nome do restaurante é: {restaurante.name.title()} o tipo de comida é: {restaurante.tipo_cozinha}")
restaurante.atendimentos()
restaurante.pessoas_atendidas = 10
restaurante.atendimentos()
restaurante.pessoas_servidas(30)
restaurante.atendimentos()
restaurante.incrementa_servidos(100)
restaurante.atendimentos()
