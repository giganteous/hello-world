"""sample test"""
import unittest

from hello import hello

class TestHello(unittest.TestCase):
    """sample test"""

    def test_world(self):
        """sample test"""
        self.assertEqual(hello('world'), 'hello world')

    def test_world_unicode(self):
        """sample test with unicode"""
        self.assertEqual(hello(u'world'), u'hello world')

    def test_fail1(self):
        self.fail("Instant misery1!")

    def test_fail2(self):
        self.fail("Instant misery2!")

    def test_fail3(self):
        self.fail("Instant misery3!")

    def test_fail4(self):
        self.fail("Instant misery4!")

    def test_fail5(self):
        self.fail("Instant misery5!")
