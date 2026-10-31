# abstraction in python is an oops concept .that hides implementation details and shows only essential features to the user.


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

    
    

