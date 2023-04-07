import unittest
from unittest.mock import MagicMock
from time_it import *

class TestTimeItDecorator(unittest.TestCase):
    def test_decorator(self):
        @time_it
        def my_function():
            time.sleep(1)
            return "done"
        
        mock_start_time = 100
        mock_end_time = 101.5
        
        with unittest.mock.patch("time.time", side_effect=[mock_start_time, mock_end_time]):
            result = my_function()
        
        self.assertEqual(result, "done")
        self.assertEqual(
            unittest.mock.MagicMock.call_args_list[0],
            unittest.mock.call()
        )
        self.assertEqual(
            unittest.mock.MagicMock.call_args_list[1],
            unittest.mock.call()
        )
        print_mock_calls = [unittest.mock.call(f"Execution time: {mock_end_time - mock_start_time} seconds")]
        self.assertEqual(
            unittest.mock.MagicMock.mock_calls,
            print_mock_calls
        )


