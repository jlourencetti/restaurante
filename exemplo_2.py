class Car():

    def __init__(self, make, model, year):
        """Inicializa os atributos que descrevem em carro"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_desriptive_name(self):
        """Devolve um nome descritivo, formatado de modo elegante."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Exibe uma frase que mostra a milhagem do carro"""
        print(f"This car has {self.odometer_reading} miles on it.")

    # Modificando o valor de um atributo com um método
    def update_odometer(self, km):
        """Define o valor de leitura do hodômetro com o valor especificdo
           Rejeita a alteração se for tentativa de definir um valor menor para o hodômetro."""
        if km >= self.odometer_reading:
            self.odometer_reading = km
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, km):
        """Soma a quantidade especifica ao valor de leitura do hodômetro."""
        self.odometer_reading += km
    

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_desriptive_name())

my_new_car.update_odometer(23500)
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()

""" # Modificando o valor de um atributo diretamente.
#my_new_car.odometer_reading = 23000
my_new_car.read_odometer()

# Modificando o valor de um atributo com um método
my_new_car.update_odometer(19)
my_new_car.read_odometer() """