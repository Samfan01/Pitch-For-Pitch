import unittest
from app.models import Pitch

class PitchModelTest(unittest.TestCase):
    def setUp(self):
        self.new_pitch = Pitch(pitch = 'people lie')
        
    # def tearDown(self):
    #     Pitch.delete()
        
    def test_init(self):
        self.assertEquals(self.new_pitch.pitch,'people lie')