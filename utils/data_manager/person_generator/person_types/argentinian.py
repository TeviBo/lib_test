import random

from utils.data_manager.person_generator.person_types.person import Person


class ARGGenerator(Person):
    def __init__(self):
        super().__init__('Argentina', 'AR', 'DNI')

    def generate_person(self):
        document = str(random.randint(10000000, 100000000))
        self.person.update({'document': document})
        return self.person
