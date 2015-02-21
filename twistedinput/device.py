from __future__ import unicode_literals
from twisted.internet.abstract import FileDescriptor
from twisted.internet import fdesc

class EventDevice(FileDescriptor):
    """
    """

    __device = None

    connected = 1

    reading = None
    backToReading = None

    def __init__(self, protocol, device, reactor = None):
        FileDescriptor.__init__(self, reactor = reactor)
        self.protocol = protocol
        self.protocol.makeConnection(self)
        self.__device = open(device, "r+w+")

        self.reading = False
        self.backToReading = False

    def fileno(self):
        return self.__device.fileno()

    def doRead(self):
        return fdesc.readFromFD(self.fileno(), self.protocol.dataReceived)

    def writeSomeData(self, data):
        rw = fdesc.writeToFD(self.fileno(), data)
        if rw == len(data) and self.backToReading:
            self.backToReading = False
            self.startReading()
        return rw

    def connectionLost(self, reason):
        FileDescriptor.connectionLost(self, reason)
        self.__device.close()
        self.protocol.connectionLost(reason)

    def write(self, data):
        if self.reading:
            self.backToReading = True
        self.stopReading()
        FileDescriptor.write(self, data)

    def startReading(self):
        self.reading = True
        FileDescriptor.startReading(self)

    def stopReading(self):
        self.reading = False
        FileDescriptor.stopReading(self)
