from __future__ import unicode_literals
from defines import *
from zope.interface import implements
from interfaces import IMapping



class BaseMapping(object):

    implements(IMapping)

    inputMapping = None

    def __init__(self):
        self.inputMapping = self.getMapping()

    def getHandler(self, event):
        return self.inputMapping[event.type][event.code]

    def getMapping(self):
        return {}

class BaseEventMapping(BaseMapping):

    def getMapping(self):
        return {
            EV_SYN          : self.getSynMapping(),
            EV_KEY          : self.getKeyMapping(),
            EV_REL          : self.getRelMapping(),
            EV_ABS          : self.getAbsMapping(),
            EV_MSC          : self.getMscMapping(),
            EV_SW           : self.getSwMapping(),
            EV_LED          : self.getLedMapping(),
            EV_SND          : self.getSndMapping(),
            EV_REP          : self.getRepMapping(),
            EV_FF           : self.getFfMapping(),
            EV_PWR          : self.getPwrMapping(),
            EV_FF_STATUS    : self.getFfStartusMapping(),
            EV_MAX          : self.getMaxMapping(),
            EV_CNT          : self.getCntMapping()}

    def getSynMapping(self):
        return {
            SYN_REPORT      : "synchronizationReport",
            SYN_CONFIG      : "synchronizationConfig",
            SYN_MT_REPORT   : "synchronizationMtReport",
            SYN_DROPPED     : "synchronizationDropped"}

    def getKeyMapping(self):
        return {}

    def getRelMapping(self):
        return {}

    def getAbsMapping(self):
        return {}

    def getMscMapping(self):
        return {}

    def getSwMapping(self):
        return {}

    def getLedMapping(self):
        return {}

    def getSndMapping(self):
        return {}

    def getRepMapping(self):
        return {}

    def getFfMapping(self):
        return {}

    def getPwrMapping(self):
        return {}

    def getFfStartusMapping(self):
        return {}

    def getMaxMapping(self):
        return {}

    def getCntMapping(self):
        return {}

class BaseJoystickMapping(BaseMapping):
    pass

class GamepadEventMapping(BaseEventMapping):

    def getKeyMapping(self):
        return {
            BTN_TRIGGER     : "button1",
            BTN_THUMB       : "button2",
            BTN_THUMB2      : "button3",
            BTN_TOP         : "button4",
            BTN_TOP2        : "triggerLeft1",
            BTN_PINKIE      : "triggerRight1",
            BTN_BASE        : "triggerLeft2",
            BTN_BASE2       : "triggerRight2",
            BTN_BASE3       : "button9",
            BTN_BASE4       : "button10",
            BTN_BASE5       : "buttonJoystickLeft",
            BTN_BASE6       : "buttonJoystickRight"}

    def getAbsMapping(self):
        return {
            ABS_X           : "joystickLeftX",
            ABS_Y           : "joystickLeftY",
            ABS_Z           : "joystickRightX",
            ABS_RZ          : "joystickRightY",
            ABS_HAT0X       : "dpadX",
            ABS_HAT0Y       : "dpadY"}

    def getMscMapping(self):
        return {
            MSC_SERIAL      : "miscSerial",
            MSC_PULSELED    : "miscPulseLed",
            MSC_GESTURE     : "miscGesture",
            MSC_RAW         : "miscRaw",
            MSC_SCAN        : "miscScan",
            MSC_MAX         : "miscMax"}

