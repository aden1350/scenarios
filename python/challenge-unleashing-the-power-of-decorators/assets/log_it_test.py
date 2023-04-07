import unittest
import logging
import os
import sys
sys.path.append("/home/labex/project")
from log_it import *
import re

class TestLogItDecorator(unittest.TestCase):
    def setUp(self):
        if os.path.exists('log.txt'):
            os.remove('log.txt')
    
    def test_decorator(self):
        @log_it
        def my_function():
            return "done"
        
        result = my_function()
        self.assertEqual(result, "done")
        
        with open('log.txt') as log_file:
            log_content = log_file.read()
        
        expected_log_content = f"Timestamp: <timestamp>, Function: my_function, Arguments: (), {{}}\n"
        actual_log_content = log_content.replace('\n', '')
        self.assertIn(expected_log_content, actual_log_content)

if __name__ == "__main__":
    unittest.main()
