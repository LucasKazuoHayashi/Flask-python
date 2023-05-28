class Person:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        self.imc = 0.0
        self.imcDescription = ""

    def getHeight(self):
        return self.height

    def setHeight(self, height):
        self.height = height

    def getWeight(self):
        return self.weight

    def setWeight(self, weight):
        self.weight = weight

    def getImc(self):
        return self.imc

    def setImc(self, imc):
        self.imc = imc

    def getImcDescription(self):
        return self.imcDescription

    def setImcDescription(self, imcDescription):
        self.imcDescription = imcDescription