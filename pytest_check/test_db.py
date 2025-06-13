import pytest
from db import Database

@pytest.fixture
def db():
    database = Database()
    yield database   ### how it diff from what is in main ?
    database.data.clear() ### what does it to ?

def test_add_user(db):
    db.add_user(1, "Alice")
    assert db.get_user(1) == "Alice"

def test_add_duplicate(db):
    db.add_user(1, "Alice")
    with pytest.raises(ValueError, match="User already exists"):
        db.add_user(1, "Bob")

def test_delete_user(db):
    db.add_user(1, "Alice")
    db.add_user(2, "Bob")
    db.delete_user(1)
    assert db.get_user(1) == None