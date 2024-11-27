import pytest
from .pets_repository import PetsRepository
from src.models.sqlite.settings.connection import db_connection_handler
from .people_repository import PeopleRepository

db_connection_handler.connect_to_db()


@pytest.mark.skip(reason="Interacao com o banco de dados")
def test_list_pets():
    repo = PetsRepository(db_connection_handler)
    response = repo.list_pets()
    print(response)


@pytest.mark.skip(reason="Interacao com o banco de dados")
def test_delete_pet():
    name = "belinha"
    repo = PetsRepository(db_connection_handler)
    repo.delete_pets(name)


@pytest.mark.skip(reason="Interacao com o banco de dados")
def test_insert_person():
    first_name = "teste name"
    second_name = "test last name"
    age = 77
    pet_id = 2

    repo = PeopleRepository(db_connection_handler)
    repo.insert_people(first_name, second_name, age, pet_id)
