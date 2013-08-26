from __future__ import unicode_literals
from zope.interface import Interface

class IMapping(Interface):

    def getHadler(event):
        """
        return name of mehod for handle event
        """

class IEventFactory(Interface):

    def buildEvent(data):
        """
        return instance of event initialize with data
        """

    def eventSize():
        """
        return size of event in bytes
        """
