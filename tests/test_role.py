import unittest
from app.models import Role


class RoleModelTest(unittest.TestCase):
    def setUp(self):
        self.new_role = Role(name='Admin')
        
    # def tearDown(self):
    #     Role.delete()
        
    def test_init(self):
        self.assertEquals(self.new_role.name,'Admin')