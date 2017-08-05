import unittest

from lwotai.labyrinth import Labyrinth
from lwotai.saver import Saver


class SaverTest(unittest.TestCase):

    def test_save_suspend_file(self):
        """Tests that the suspend file can be saved without error"""
        saver = Saver()
        app = Labyrinth(1, 1)
        saver.save_suspend_file(app)