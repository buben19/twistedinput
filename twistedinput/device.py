from __future__ import unicode_literals
from twisted.internet.abstract import FileDescriptor
from twisted.internet import fdesc

class EventDevice(FileDescriptor):
    """
    """

    __device = None

    def __init__(self, protocol, device):
        FileDescriptor.__init__(self)
        self.protocol = protocol
        self.protocol.makeConnection(self)
        self.__device = open(device)

    def fileno(self):
        return self.__device.fileno()

    def doRead(self):
        return fdesc.readFromFD(self.fileno(), self.protocol.dataReceived)
