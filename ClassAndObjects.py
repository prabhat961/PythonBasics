i, j = 15, 25 # Global Variable
class MyClass: #class Creation
    #Declaring Variables in the class:
    a,b = 100,200 # Class Variable
#Creating Methods with these  Variabless
    def printSum(self):
        print(self.a + self.b)

    def printProduct(self):
        print(self.a * self.b)

# Creating Menthods/Functions
    def MyFunction(self):
        pass
    def printName(self,name):
        print("Name is:",name)

    #Creating Static Methods
    @staticmethod
    def printMethod():
        print("This is a Static Method")

    def accesVariable(self, x, y):
        print(x + y) # access Local Variable
        print(self.a + self.b) # Acess CLass Variable
        print(i + j) #Acess Global Variable

# Object creation of that class
mc = MyClass()

#calling function of that class
mc.MyFunction()
mc.printName('nidhi')
MyClass.printMethod()
mc.printSum()
mc.printProduct()
mc.accesVariable(15, 5)