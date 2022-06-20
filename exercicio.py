class Restaurante():

    def __init__(self, name, tipo_cozinha ):
        self.name = name
        self.tipo_cozinha = tipo_cozinha

    def descrever_restaurante(self):
        print(f"Esse restaurante se chama {self.name} e é {self.tipo_cozinha} ")

    def restaurante_aberto(self):
        print(f"O restaurante {self.name} com cozinha {self.tipo_cozinha} esta aberto!")

    
meu_restaurante = Restaurante("Guilere", "Italiano")

meu_restaurante_2 = Restaurante('Draft', "alemã")

print(f"O restaurante de semana {meu_restaurante.name.title()}")
print(f"O tipo de comida do restaurante {meu_restaurante.name.title()} é {meu_restaurante.tipo_cozinha.title()} ")

meu_restaurante.descrever_restaurante()
meu_restaurante.restaurante_aberto()

meu_restaurante_2.descrever_restaurante()