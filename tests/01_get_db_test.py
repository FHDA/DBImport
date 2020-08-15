"""Test get_db.

This module tests the correctness and exceptions of InsertData/get_db()
"""


import sys
sys.path.append('./src')
from InsertData import get_db
from configparser import ConfigParser
from pathlib import Path
import pymongo
import pytest

env_config = ConfigParser()
env_config.read(Path.cwd() / 'config' / 'setting.config')
mongo_config = env_config['MongoDB']

def test_get_db_existence():
    """Test if get_db() return the correct type."""
    db = get_db()
    assert isinstance(db, pymongo.database.Database)


@pytest.mark.skip(reason = "Mongoclient does not throw any exceptions or errors currently")
def test_get_db_with_worong_username():
    """Test if get_db() raises an exception if the username is incorrect."""
    mongo_config['Mongo_User'] = 'WrongUserName'
    with pytest.raises(Exception):
        db = get_db()


@pytest.mark.skip(reason = "Mongoclient does not throw any exceptions or errors currently")
def test_get_db_with_worong_password():
    """Test if get_db() raises an exception if the password is incorrect."""
    mongo_config = env_config['MongoDB']
    mongo_config['Mongo_Password'] = 'WrongPassword'
    with pytest.raises(Exception):
        db = get_db()
