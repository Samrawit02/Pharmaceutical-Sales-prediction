import os
import sys
import unittest
import pandas as pd



sys.path.append(os.path.abspath(os.path.join('../scripts')))
from file_handler import FileHandler

class TestFileHandler(unittest.TestCase):
    def setUp(self) ->pd.DataFrame:
        self.fileHelp = FileHandler()

    def test_to_csv(self):
        df = pd.DataFrame({'col1': [1, 2, 1], 'col2': [3, 4, 3]})
        self.fileHelp.to_csv(df, './test.csv', False)
        df2 = pd.to_csv('test.csv')
        self.assertEqual(df.shape, df2.shape)

    def test_read_csv(self):
        df = self.fileHelp.read_csv('test.csv')
        df2 = pd.read_csv('test.csv')
        self.assertEqual(df.shape, df2.shape)


if __name__ == '__main__':
  unittest.main()