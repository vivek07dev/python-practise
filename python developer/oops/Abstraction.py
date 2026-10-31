

# from abc import  Abc ,abstractmethod
# class vehicle (Abc):
#     @abstractmethod
#     def start(self):
#         pass
#     def stop(self):
#         self.stop

# class car (vehicle):
#     def start(self):
#        print("car is starting")
#     def stop(self):
#        print("car is stopping")


# class bike (vehicle):
#     def start (self):
#         print(bike is self.starting)
#     def stop(self):
#         print("bike is stopping")


# s1= car()      
# s2 = vehicle()
# s1.start()
# s2.stop()
# s1.start()
# s2.start()
# s2.miles()





from abc import  ABC ,abstractmethod

class company:
    @abstractmethod

    def salary(self):
        pass

class Developer(company):
    def salary(self):
        print("developer salary 67k")

class Tester:
    def salary(self):
        print("tester salary 56k")  

class Designer:
    def salary(self):
        print("designer salary 45k")

vivek = Developer()
vivek.salary()
neeraj = Tester()
neeraj.salary()
suraj = Designer()
suraj.salary()

    
    

