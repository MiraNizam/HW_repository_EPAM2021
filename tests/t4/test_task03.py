from hw4.task_3_get_print_output import my_precious_logger

def test_case_my_precious_logger_stdout(capsys):
    text = "text doesn't start with error so it should return stdout"
    my_precious_logger(text)
    out, err = capsys.readouterr()
    assert out == text + "\n"
def test_case_my_precious_logger_stderr(capsys):
    text = "error text, it should raise stderr"
    my_precious_logger(text)
    out, err = capsys.readouterr()
    assert err == text + "\n"

