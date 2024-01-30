from faker import Faker

from utils.data_manager.data_generator import generate_random_phone_valid


class Person:
    _fake = Faker()

    def __init__(self, nationality, nationality_code, document_type):
        self.person = {
            'last_name': self._fake.last_name(),
            'first_name': self._fake.first_name(),
            'email': self._fake.email().replace("-", ""),
            'doc_type': document_type,
            'nationality': nationality,
            'document': '',
            'nationality_code': nationality_code,
            'phone': generate_random_phone_valid(),
            'password': '122222'
        }
