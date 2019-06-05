
def printFileName():
    print("Produkt")

class Produkt:
    name="",
    weight=None,
    value=None

    def __init__(self,name,weight,value):
        self.name=name
        self.value=value
        self.weight=weight

    def getName(self):
        return self.name

    def setName(self,name):
        self.name=name

    def getWeight(self):
        return self.weight

    def setWeight(self, weight):
        self.weight=weight

    def getValue(self):
        return self.value

    def setValue(self,value):
        self.value=value

    def printProduct(self):
        print("Name= {}, Weight= {}, Value= {}.".format(self.name,self.weight,self.value))