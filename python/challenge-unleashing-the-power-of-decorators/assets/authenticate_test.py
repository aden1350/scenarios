import unittest
from unittest.mock import patch
from authenticate import *

class TestAuthenticateDecorator(unittest.TestCase):
    def test_decorator_with_valid_credentials(self):
        @authenticate
        def my_function():
            return "done"
        
        with patch('builtins.input', side_effect=['myusername', 'mypassword']):
            result = my_function()
        
        self.assertEqual(result, "done")
    
    def test_decorator_with_invalid_credentials(self):
        @authenticate
        def my_function():
            return "done"
        
        with patch('builtins.input', side_effect=['wrongusername', 'wrongpassword']):
            with self.assertRaises(Exception):
                my_function()
