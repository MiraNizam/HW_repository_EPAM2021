import os
from tempfile import NamedTemporaryFile

import pytest

from hw4.task_1_read_file import read_magic_number

filepath = os.path.dirname(__file__)

def call_func_with_temp_file(test_func, text):
    """The func creates temp_file, write text in this file and call it as argument"""
    with NamedTemporaryFile(prefix=filepath, mode="w") as temp_file:
        temp_file.write(text)
        temp_file.seek(0)
        return test_func(temp_file.name)

def test_file_without_errors():
    assert call_func_with_temp_file(read_magic_number, "2")

def test_empty_file():
    with pytest.raises(ValueError):
        call_func_with_temp_file(read_magic_number, "")

def test_for_wrong_format():
    with pytest.raises(ValueError):
        call_func_with_temp_file(read_magic_number, "This will throw an error")

