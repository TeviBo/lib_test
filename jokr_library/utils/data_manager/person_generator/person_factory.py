from jokr_library.utils.data_manager.person_generator.person_types.argentinian import ARGGenerator
from jokr_library.utils.data_manager.person_generator.person_types.peruvian import PEGenerator


class PersonFactory:

    def __init__(self):
        self.person = {
            "argentina": ARGGenerator,
            "peru": PEGenerator,
        }

    def get_person_generator(self, country):
        person_generator = self.person[country.lower()]()
        return person_generator
