import os
import random
import unittest
import subprocess
from client import ann_client


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        #os.system("python2 read_server.py &")
        subprocess.call(["python2", "read_server.py"])
        self.client = ann_client()

    def test_server(self):
        # run server
        try:
            rec = self.client.call_ann("Hallo Welt")
            print "Jakob",rec
        finally:
            self.client.disconnect()

        assert True

if __name__ == '__main__':
    unittest.main()
