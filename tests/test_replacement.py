import unittest
from services import replacement


class TestReplacement(unittest.TestCase):

    def test_get_configuration(self):
        actual = replacement.get_configuration('./data/config.txt')
        expected = {
            'a' : 'z',
            'b' : 'y',
            'c' : 'x',
        }
        self.assertEqual(actual, expected)

    def test_get_text(self):
        actual = replacement.get_text('./data/text.txt')
        expected = ['djf#aemfaofna%\n', 'b#sjf_ansvo!\n', 'cnhjrfyjvth3nxr']
        self.assertEqual(actual, expected)

    def test_processes_text(self):
        actual = replacement.processes_text(['djf#aemfaofna%\n', 'b#sjf_ansvo!\n', 'cnhjrfyjvth3nxr'],
        ['a', 'b', 'c'], ['z', 'y', 'x'])
        expected = ['djf#zemfzofnz%\n', 'y#sjf_znsvo!\n', 'xnhjrfyjvth3nxr']
        self.assertEqual(actual, expected)

    def test_delete_line_break(self):
        actual = replacement.delete_line_break('djf#zemfzofnz%\n')
        expected = 'djf#zemfzofnz%'
        self.assertEqual(actual, expected)

    def test_invert_of_text(self):
        actual = replacement.invert_of_text(['name', 'good', 'pokemon'])
        expected = ['nomekop', 'doog', 'eman']
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
