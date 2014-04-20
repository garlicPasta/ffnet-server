import os
import random
import unittest
import subprocess
import time
from client import ann_client


class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        #os.system("python2 frontend.py &")
        print("Run frontend end server")
        subprocess.Popen(["python2", "queue_server.py"])
        time.sleep(3)
        self.client = ann_client()

    def test_server(self):
        # run server
        try:
            msg = []
            rec = self.client.call_ann((3, [3, 5, "c", "d"]))
            print "Jakob", rec
        finally:
            self.client.disconnect()
            subprocess.call(["pkill", "python2"])
        assert True


if __name__ == '__main__':
    unittest.main()
