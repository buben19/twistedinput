# twistedinput

### Reading input devices using [Twisted](http://twistedmatrix.com/trac/) framework

Twisted is Python framework for asynchronous IO and event driven programming.
Twistedinput is library for this framework for interacting input devices, such
as gamepads, joysticks, mouses and etc in asynchrounous fashion.

An input event is represented by standar input_event structure defined in
linux/input.h header file. Twistedinput also supports js_event for joysticks
defined in linux/joystick.h.

Communication protocol is intended for handling only those event, which you are
interested to.

```pycon
from twistedinput.device import EventDevice
from twistedinput.protocol import EventProtocol
from twistedinput.factory import InputEventFactory
from twistedinput.mapping import GamepadEventMapping
from twisted.internet import reactor

class MyGamepad(EventProtocol):

    def button1(self, event):
        print "button 1:", event.value

EventDevice(
    MyGamepad(
        InputEventFactory(),
        GamepadEventMapping()),
    "/dev/input/event13").startReading()
reactor.run()
```


### Event Mapping

Accordint to linux/input.h header file. any input event consists from four
fields:

    timestamp
    type
    code
    value

Type and code fields has defined values that can take. But these values are
meaningless for describing physical buttons.
For example, when I press button 1 on my gamepad, input_event with type EV_KEY
and code BTN_TRIGGER is emitted. But I pressed button 1, not trigger.

Event mapping basicaly allows you to write a driver for your device. Mapping
simply defines, that event with type EV_KEY and code BTN_TRIGGER should be
handled in button1 method, for example. For different device you can define
different event mappings and handle event by methods with logic names.

If handler method defined in the used mapping doesn't exist in the protocol,
event is ignored.

### Handling Events Without Mapping

In the EventProtocol constructor eventMapping is optional parameter. If is
omnited, you have to override eventReceived method and handle event by yourself.

### Event Factory

Factory is simple object which takes bytes representing data stream emmited by
event and returns object represnting this event.
It also provides information of size of the event.
