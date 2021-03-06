import unittest,TesCase
from . import Comment

class CommentModelTest(unittest.TesCase):
    def setUp(self):
        self.new_comment = Comment(comment = 'Good pitch')
        
    def tearDown(self):
        Comment.delete()
        
    def test_init(self):
        self.assertEquals(self.new_comment.comment,'Good pitch')