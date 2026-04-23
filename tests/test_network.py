import sys, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]/'src'))
from syncpath.domain import NetworkWindow
from syncpath.network import Network

class NetworkTests(unittest.TestCase):
    def test_offline(self):
        self.assertEqual(Network([NetworkWindow(0,100,False)]).transmit(1)[2],'offline')
    def test_packet_loss(self):
        self.assertEqual(Network([NetworkWindow(0,100,True,10,1.0)]).transmit(1)[2],'packet-loss')
    def test_crossing_outage(self):
        net=Network([NetworkWindow(0,10,True,20),NetworkWindow(10,100,False)])
        self.assertEqual(net.transmit(2)[2],'handoff-interruption')
