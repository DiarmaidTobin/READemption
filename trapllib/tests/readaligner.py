import unittest
import sys
from io import StringIO
sys.path.append(".")
from trapllib.readmapper import ReadMapper

class TestReadMapper(unittest.TestCase):

    def setUp(self):
        self.read_mapper = ReadMapper("segemehl")

    @unittest.skip("TODO")
    def test_build_index(self):
        self.build_index()

    def test_run_mappings(self):
        pass

if __name__ == "__main__":
    unittest.main()
