import unittest
import logging
import os
import sys
sys.path.append("/home/labex/project")
from log_it import *

class TestLogItDecorator(unittest.TestCase):
    def setUp(self):
        if os.path.exists('log.txt'):
            os.remove('log.txt')
    
    def test_decorator_should_log_function_call_to_file(self):
        @log_it
        def my_function():
            return "done"

        result = my_function()
        self.assertEqual(result, "done")

        with open('log.txt') as log_file:
            log_content = log_file.read()

        expected_log_content = f"Timestamp: {time.time()}, Function: my_function, Arguments: (), {{}}\n"
        self.assertIn(expected_log_content, log_content)

    def test_decorator_should_log_function_call_with_args_to_file(self):
        @log_it
        def my_function(a, b, c):
            return a + b + c

        result = my_function(1, 2, 3)
        self.assertEqual(result, 6)

        with open('log.txt') as log_file:
            log_content = log_file.read()

        expected_log_content = f"Timestamp: {time.time()}, Function: my_function, Arguments: (1, 2, 3), {{}}\n"
        self.assertIn(expected_log_content, log_content)

    def test_decorator_should_log_function_call_with_kwargs_to_file(self):
        @log_it
        def my_function(a, b, c):
            return a + b + c

        result = my_function(a=1, b=2, c=3)
        self.assertEqual(result, 6)

        with open('log.txt') as log_file:
            log_content = log_file.read()

        expected_log_content = f"Timestamp: {time.time()}, Function: my_function, Arguments: (), {{'a': 1, 'b': 2, 'c': 3}}\n"
        self.assertIn(expected_log_content, log_content)

if __name__ == '__main__':
    unittest.main()
