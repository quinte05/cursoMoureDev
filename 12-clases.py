### Classes ###

# Definición

class MyEmptyPerson:
    pass #comando para que no falle y quede vacio

#print(MyEmptyPerson)
#print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias = "sin alias"):
        Person.namee = name
        Person.surnemee = surname
        Person.fullname = f"{name} {surname} ({alias})"
    
    def walk(self):
        print(f"{self.fullname} Esta caminando")

my_person = Person("Andres", "Quintero")

print(f"{my_person.namee} {my_person.surnemee}")
print(f"{my_person.fullname}")

my_person.walk()

my_other_person = Person("Sandra", "Valencia", "la mona")

print(f"{my_other_person.fullname}")
my_other_person.walk()

my_other_person.fullname = "Rafa Moncada (el loco de las bicis)"
print(my_other_person.fullname)
my_other_person.walk()

"""class MyEmptyPerson:
    pass  # Para poder dejar la clase vacía


print(MyEmptyPerson)
print(MyEmptyPerson())

# Clase con constructor, funciones y popiedades privadas y públicas


class Person:
    def __init__(self, name, surname, alias="Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"  # Propiedad pública
        self.__name = name  # Propiedad privada

    def get_name(self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} está caminando")


my_person = Person("Brais", "Moure")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Brais", "Moure", "MoureDev")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Héctor de León (El loco de los perros)"
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)"""