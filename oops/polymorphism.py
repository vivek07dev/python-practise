# polymorphism means one name with many forms

class GrandParent:
    def Age (self):
        print("56")

class Parent:
    def Age (self):
        print("40")

def detail(Person):
    Person.Age()
G1 = GrandParent()
P1 = Parent()
G1.Age()
P1.Age()