class perro():
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
    
    def ladrar(self):
        if self.peso >= 8:
            print("{} te dice: GUAU, GUAU".format(self.nombre))
        if self.peso < 8:
            print("{} te dice: Guau, Guau".format(self.nombre))
    
    def __str__(self):
        return "Soy el perro {}, tengo {} años y peso {} Kg.".format(self.nombre, self.edad, self.peso)

class PerroAsistencia(perro):
    def __init__(self, nombre, edad, peso, amo):
        perro.__init__(self, nombre, edad, peso)
        self.amo = amo
        self.__trabajando = False
    
    def __str__(self):
        return "Soy el perro {}, tengo {} años y peso {} Kg, mi dueño es {}.".format(self.nombre, self.edad, self.peso, self.amo)
    
    def pasear(self):
        print("Ayudo a mi dueño, {}, a pasear".format(self.amo))
    
    def ladrar(self):
        if self.__trabajando == True:
            print("shhhh, no puedo ladrar, estoy trabajando")
        else:
            perro.ladrar(self)
    
    def trabajando(self, valor = None):
        if valor == None:
            return self.__trabajando
        else:
            self.__trabajando = valor
            

toby = perro("Toby", 3, 12)
miku = perro("Miku", 10, 2)
roque = PerroAsistencia("Roque", 4, 8, "Jimmy")
toby.ladrar()
miku.ladrar()
roque.ladrar()
roque.pasear()
print(toby)
print(miku)
print(roque)