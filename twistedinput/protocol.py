from __future__ import unicode_literals
from twisted.internet.protocol import Protocol



class EventProtocol(Protocol):

    # factory for building events
    __eventFactory = None

    # define which method will be called at given event
    __eventMapping = None

    # buffering event bytes
    __buffer = None

    def __init__(self, eventFactory, eventMapping = None):
        self.__eventFactory = eventFactory
        self.__eventMapping = eventMapping
        self.__buffer = str()

    def dataReceived(self, data):
        lastIndex = 0
        self.__buffer += data
        while lastIndex < len(self.__buffer) and \
                len(self.__buffer) >= self.__eventFactory.eventSize():
            self.eventReceived(
                self.__eventFactory.buildEvent(
                    self.__buffer[lastIndex : lastIndex + self.__eventFactory.eventSize()]))
            lastIndex += self.__eventFactory.eventSize()
        self.__buffer = self.__buffer[lastIndex:]

    def eventReceived(self, event):
        handler = None
        try:
            handler = self.__eventMapping.getHandler(event)
        except KeyError:

            # mapping doesn't support handler for this event
            pass

        if hasattr(self, handler) and callable(getattr(self, handler)):
            getattr(self, handler)(event)

class EventSniffer(EventProtocol):
    """
    tool for reading data. Developing purposes
    """

    def __init__(self, eventFactory):
        EventProtocol.__init__(self, eventFactory, None)

    def eventReceived(self, event):
        print "event: %s" % (unicode(event),)
