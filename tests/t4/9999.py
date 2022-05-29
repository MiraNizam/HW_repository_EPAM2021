import os
from tempfile import NamedTemporaryFile

filepath = os.path.dirname(os.path.abspath(__file__))


def call_func_with_temp_file(text):
    """The func creates temp_file, write text in this file and call it as argument"""
    with NamedTemporaryFile(prefix=filepath, mode="w") as temp_file:
        temp_file.write(text)
        temp_file.seek(0)
        return temp_file.name


def read_magic_number(path: str) -> bool:
    """ Read the first line of the file. If the first line is a number in
     an interval [1, 3) return True, if other number False, else the function raises Value Error.
    """
    try:
        with open(path) as f:
            line = f.readline().strip()
    except Exception as error:
        raise ValueError(f"We got error {error}")

    if line:
        try:
            return 1 <= float(line) < 3
        except ValueError:
            pass
    return False

read_magic_number(call_func_with_temp_file("ldfjfjghfkl"))