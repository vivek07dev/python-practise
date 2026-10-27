#  # single inheritance

# class parent:
#     def beating (self):
#         print("child is crying")
# class child (parent):
#     def laughing(self):
#         print("ha ha haan") 
# tarun = child() 
# tarun. laughing()  
# tarun.beating()       


# #multiple inheritance

# class Mother:
#     def calling(self):
#         print("Roti khalo")
# class father:
#     def beating (self):
#         print("child is crying")
# class child (Mother,father):
#     def laughing(self):
#         print("ha ha haan") 
# tarun = child() 
# tarun. laughing()  
# tarun.beating()   
# tarun.calling ()  

# # Multilevel inheritance...
class GrandPaent:
    def method(self):
        print("GrandParent method")
        
class parent(GrandPaent):
    def Parent(self):        
       print("GrandParent")
    def method2(self):
        print("parent method")

class child(parent):   
    def method3(self):
        print("child method") 

obj = child()    
obj.method()   
obj.method2()
obj.method3() 
 
