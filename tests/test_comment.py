import unittest
from app.models import Comment, Pitch
from app import db

class TestPitchComment(unittest.TestCase):

    def setUp(self):
        self.new_pitch = Pitch(pitch = "smile more", category='family')
        self.new_comment = Comment(comment = "hello rita", pitch=self.new_pitch)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,"hello rita")
        self.assertEquals(self.new_comment.pitch,self.new_pitch,'smile more')