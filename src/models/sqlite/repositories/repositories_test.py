import pytest
from .pets_repository import PetsRepository
from src.models.sqlite.settings.connection import db_connection_handler


# db_connection_handler.connect_to_db()


@pytest.mark.skip(reason="Interacao com o banco de dados")
def test_list_pets():
    repo = PetsRepository(db_connection_handler)
    response = repo.list_pets()
    print(response)


def test_delete_pet():
    name = "belinha"
    repo = PetsRepository(db_connection_handler)
    repo.delete_pets(name)
