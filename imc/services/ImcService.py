class ImcService:
    def __init__(self):
        pass

    @staticmethod
    def calculateImc(person):
        person.setImc(person.getWeight() / (person.getHeight() ** 2))

    @staticmethod
    def resultIMC(person):
        person.setImcDescription("Obesidade")
        if person.getImc() < 18.5:
            person.setImcDescription("Magreza")
        elif person.getImc() < 24.9:
            person.setImcDescription("Normal")
        elif person.getImc() < 30:
            person.setImcDescription("Sobrepeso")

    def returnImc(self, person):
        self.calculateImc(person)
        self.resultIMC(person)