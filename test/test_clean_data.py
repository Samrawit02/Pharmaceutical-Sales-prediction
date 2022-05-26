from msilib.schema import Class
import os
import sys
import unittest
import pandas as pd
import pandas.api.types as ptypes
from pandas.api import types

sys.path.append(os.path.abspath(os.path.join('../scripts')))

from clean_data import Clean_data


class TestCleanData(unittest.TestCase):

    def setUp(self)-> pd.DataFrame:
        self.cleaner = Clean_data()
    
    def testDropDuplicate(self):
        df = pd.DataFrame({'col1': [3, 4, 3], 'col2': [3, 4, 3]})
        df = self.cleaner.drop_duplicate(df)
        self.assertEqual(df.shape, (2, 2))

    def test_convert_to_string(self):
        df = pd.DataFrame({'col1': ["hello", "world"]})
        df = self.cleaner.convert_to_string(df, ['col1'])
        self.assertTrue(df['col1'].dtype == "string")

    def test_convert_to_datetime(self):
        df = pd.DataFrame({'col1': ["2018-01-05", "2018-01-06"]})
        df = self.cleaner.convert_to_datetime(df, ['col1'])
        self.assertTrue(type(df['col1'].dtype == ptypes.DatetimeTZDtype))

if __name__ == '__main__':
    unittest.main()