import unittest
import logging
import os
from log_it import *

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
        self.assertIn(expected_log_content, log_content)