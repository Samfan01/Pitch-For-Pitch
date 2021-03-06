import unittest
from app.models import Comment

class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.new_comment = Comment(comment = 'Good pitch')
        
    # def tearDown(self):
    #     Comment.delete()
        
    def test_init(self):
        self.assertEquals(self.new_comment.comment,'Good pitch')