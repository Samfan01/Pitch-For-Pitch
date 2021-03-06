import unittest,TesCase
from ..models import Role


class RoleModelTest(unittest.TesCase):
    def setUp(self):
        self.new_role = Role(role='Admin')
        
    def tearDown(self):
        Role.delete()
        
    def test_init(self):
        self.assertEquals(self.new_role.role,'Admin')