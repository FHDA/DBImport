"""Test check_file_open.

This module tests the correctness and exceptions of InsertData/check_file_open()
"""

import sys
sys.path.append('./src')
from InsertData import check_file_open
import pytest

def test_check_file_open_existence_and_correctness():
    """Test if check_file_open() return the correct type and the returned dict has the right content."""
    result = check_file_open('tests/test.json')
    assert isinstance(result, dict)
    assert result


def test_check_file_open_not_exist():
    """Test if check_file_open() handles correctly with a nonexistent file."""
    with pytest.raises(FileNotFoundError):
        result = check_file_open('tests/nonexistent.json')
