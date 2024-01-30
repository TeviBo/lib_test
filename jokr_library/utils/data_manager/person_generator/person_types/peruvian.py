import random

from .person import Person


class PEGenerator(Person):

    def __init__(self):
        super().__init__('Peru', 'pe', 'DNI')

    def generate_person(self):
        document = str(random.randint(10000000, 99999999))
        self.person.update({'document': document})
        return self.person
