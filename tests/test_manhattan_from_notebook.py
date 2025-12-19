import pytest

pytest.skip(
    "Notebook kernel not available in this environment",
    allow_module_level=True
)

from nbresult import ChallengeResultTestCase

class TestManhattanFromNotebook(ChallengeResultTestCase):
    def test_manhattan(self):
        self.assertEqual(self.result.manhattan, 7)

    def test_manhattan_reverse(self):
        self.assertEqual(self.result.manhattan_reverse, 7,
                         msg="Distances can't be negative.")
