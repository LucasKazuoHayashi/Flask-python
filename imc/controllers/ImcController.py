from imc.services.ImcService import ImcService
from imc.models.Person import Person

class ImcController:
    def __init__(self):
        self.imc_service = ImcService()

    def calculate_imc(self, height, weight):
        person = Person(height, weight)
        self.imc_service.returnImc(person)

        result = {
            'height': person.getHeight(),
            'weight': person.getWeight(),
            'imc': person.getImc(),
            'imcDescription': person.getImcDescription()
        }

        return result