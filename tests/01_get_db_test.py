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
from dotenv import load_dotenv

load_dotenv()

def test_get_db_existence():
    """Test if get_db() return the correct type."""
    db = get_db()
    assert isinstance(db, pymongo.database.Database)
