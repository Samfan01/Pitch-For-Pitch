import unittest,TesCase
from ..models import Role



def setUp(self):
    self.new_role = Role(role='Admin')
    
def test_init()