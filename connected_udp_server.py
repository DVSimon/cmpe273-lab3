from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class Echo(DatagramProtocol):

    def datagramReceived(self, data, address):
        print("received %r from %s" % (data, address))
        self.transport.write(data, address)

reactor.listenUDP(9999, Echo())
reactor.run()