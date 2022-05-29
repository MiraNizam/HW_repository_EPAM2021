from hw1.task03 import find_maximum_and_minimum

def test_file_with_numbers(tmpdir):
    """Testing that def can fine min and max values"""
    created_file = tmpdir.mkdir("tempdir").join("tempfile")
    created_file.write("-88\n76\n-22\n45\n11\n70\n-99")
    assert find_maximum_and_minimum(created_file) == (76,-99)


def test_file_with_duplicate_value(tmpdir):
    """Testing if the file includes one duplicate value, min = max"""
    created_file = tmpdir.mkdir("tempdir").join("tempfile")
    created_file.write("-88\n88")
    assert find_maximum_and_minimum(created_file) == (88, -88)


def test_file_with_one_value(tmpdir):
    """Testing if the file includes one value, min = max"""
    created_file = tmpdir.mkdir("tempdir").join("tempfile")
    created_file.write("45")
    assert find_maximum_and_minimum(created_file) == (45, 45)
