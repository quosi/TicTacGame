#import pytest
import unittest
from main import TicTac

class TestGame(unittest.TestCase):
    def test_run_game(self):
        size = [*range(11)]
        self.assertTrue(TicTac(size, True))