class GrandParent:
    def age(self):
        print("68")

class Parent(GrandParent):
     def age(self):
         print("30")      
gp = GrandParent()
p = Parent()
gp.age()
p.age()


#method overriding occures when child class iherit method from parent but Implementation its own functionality