from __future__ import unicode_literals
from ctypes import *
from defines import input_event, js_event


class BaseEvent(object):

    _event = None

    def _fromBytes(self, eventBytes, eventStructure):
        if not len(eventBytes) == sizeof(eventStructure):
            raise ValueError, "data must have length of %d bytes" % \
                (sizeof(eventStructure),)
        event = eventStructure()
        memmove(addressof(event), eventBytes, sizeof(eventStructure))
        return event

    def __str__(self):
        return unicode(self).encode("utf-8")

    def __repr__(self):
        return ("<%s %s>" % (self.__class__.__name__, unicode(self))).encode("utf-8")

class InputEvent(BaseEvent):
    """
    class representing an input event
    """

    __time = None

    def __init__(self, inputEvent):
        """
        initialize input event
        input event can be stypes.Structure or string representing byte stream
        """
        self._event = self.__getInputEvent(inputEvent)

    def __getInputEvent(self, data):
        if isinstance(data, input_event):
            return data
        elif isinstance(data, str):
            return self._fromBytes(data, input_event)
        else:
            raise TypeError, "expected input_event or bytes, got %s" % \
                (type(data).__name__,)

    @property
    def time(self):
        if self.__time is None:
            self.__time = Time(self._event.time)
        return self.__time

    @property
    def type(self):
        return self._event.type

    @property
    def code(self):
        return self._event.code

    @property
    def value(self):
        return self._event.value

    @classmethod
    def size(cls):
        """
        return size of input data in bytes
        """
        return sizeof(input_event)

    def __unicode__(self):
        return "type: 0x%04x, code: 0x%04x, value: 0x%08x" % \
            (self.type, self.code, self.value & 0xffffffff)

class Time(object):

    __time = None

    def __init__(self, time):
        self.__time = time

    @property
    def seconds(self):
        return self.__time.tv_sec

    @property
    def useconds(self):
        return self.__time.tv_usec

class JoystickEvent(BaseEvent):

    def __init__(self, joystickEvent):
        self._event = self.__getJoystickEvent(joystickEvent)

    def __getJoystickEvent(self, data):
        if isinstance(data, js_event):
            return data
        elif isinstance(data, str):
            return self._fromBytes(data, js_event)
        else:
            raise TypeError, "expected js_event or bytes, got %s" % \
                (type(data).__name__,)

    @property
    def time(self):
        return self._event.time

    @property
    def value(self):
        return self._event.value

    @property
    def type(self):
        return self._event.type

    @property
    def number(self):
        return self._event.number

    def __unicode__(self):
        return "time: %d, value: 0x%04x, type: 0x%02x, number: 0x%02x" % \
            (self.time, self.value, self.type, self.number)

    @classmethod
    def size(cls):
        return sizeof(js_event)
