from main import add, devide, UserManager
import pytest

def test_add():
    assert add(3,2) == 5

def test_devide():
    assert devide(3,3) == 1

def test_devide_err():   
    """
    Test asures that devision by 0 is rassing the ValueError
    """
    with pytest.raises(ValueError, match="Can't devide by zero"):
        devide(4,0)

@pytest.fixture ### allows to create a fresh setup (instance) 
def user_manager():
    """
    Creates instance of UserManager before each test.
    """
    return UserManager()

def test_add_user(user_manager):
    assert user_manager.add_user("john", "john@ex.io") == True
    assert user_manager.get_user("john") == "john@ex.io"

def test_duplicate_user(user_manager):
    user_manager.add_user("johnA", "johnA@ex.io")
    with pytest.raises(ValueError):
       user_manager.add_user("johnA", "johnA@ex.io") 

