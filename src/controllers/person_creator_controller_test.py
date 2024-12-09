import pytest
from .person_creator_controller import PersonCreatorController


class MockPeopleRepository:
    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int):
        pass


def test_create_error():
    person_info = {
        "first_name": "Fulano123",
        "last_name": "deTal",
        "age": 30,
        "pet_id": 123,
    }

    controller = PersonCreatorController(MockPeopleRepository())

    with pytest.raises(Exception):
        controller.create(person_info)
