from unittest import TestCase
from unittest.mock import MagicMock

from urllib import request

from hw4.task_2_mock_input import count_dots_on_i

class TestCountDot(TestCase):
    def test_count_dots_on_i_for_count_symbol(self):
        url = "no link, mock will be used"
        count_dots_on_i = MagicMock(return_value=21)
        self.assertEqual(count_dots_on_i(url), 21)

    def test_count_dots_on_i_with_exception(self):
        url = "no link,mock will be used"
        request.urlopen = MagicMock(side_effect=ConnectionError)
        with self.assertRaises(ValueError, msg=f"Unreachable {url}"): count_dots_on_i(url)