# Criando e usando uma classe:
# Criando a classe DOG:
class Dog():

    def __init__(self, name, age):
        """Inicializa os atributos name e age."""
        self.name = name
        self.age = age

    def sentar(self):
        """Simula um cachorro sentando em resposta a um comando"""
        print(f"{self.name.title()} agora está sentado.")

    def rolar(self):
        """Simula um cachorro rolando em resposta a um comando."""
        print(f"{self.name.title()} rolando!")

# Criando instância
meu_cachorro = Dog('fred', 12)
print(f"Meu cachorro se chama {meu_cachorro.name.title()}.")
print(f"Meu cachorro é {meu_cachorro.age} anos.")


# Chamando metodos:
meu_cachorro.sentar()
meu_cachorro.rolar()


# Criando várias instâncias:
seu_cachorro = Dog('bily', 8)
print(f"Seu cachorro se chama {seu_cachorro.name.title()}.")
seu_cachorro.sentar()
