from __future__ import unicode_literals
from event import InputEvent, JoystickEvent
from zope.interface import implements
from interfaces import IEventFactory


class InputEventFactory(object):

    implements(IEventFactory)

    def buildEvent(self, data):
        return InputEvent(data)

    def eventSize(self):
        return InputEvent.size()

class JoystickEventFactory(object):

    def buildEvent(self, data):
        return JoystickEvent(data)

    def eventSize(self):
        return JoystickEvent.size()
