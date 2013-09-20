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
        return {
            MSC_SERIAL      : "miscSerial",
            MSC_PULSELED    : "miscPulseLed",
            MSC_GESTURE     : "miscGesture",
            MSC_RAW         : "miscRaw",
            MSC_SCAN        : "miscScan",
            MSC_MAX         : "miscMax"}

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

class KeyboardMapping(BaseEventMapping):

    def getKeyMapping(self):
        keys = {}
        keys.update(self.alphanumericKeys())
        keys.update(self.functionKeys())
        keys.update(self.directionKeys())
        keys.update(self.specialKeys())
        keys.update(self.genericKeys())
        keys.update(self.laptopKeys())
        return keys

    def alphanumericKeys(self):
        keys = {}
        keys.update(self.characterKeys())
        keys.update(self.numericKeys())
        return keys

    def characterKeys(self):
        return {
            KEY_A           : "keyA",
            KEY_B           : "keyB",
            KEY_C           : "keyC",
            KEY_D           : "keyD",
            KEY_E           : "keyE",
            KEY_F           : "keyF",
            KEY_G           : "keyG",
            KEY_H           : "keyH",
            KEY_I           : "keyI",
            KEY_J           : "keyJ",
            KEY_K           : "keyK",
            KEY_L           : "keyL",
            KEY_M           : "keyM",
            KEY_N           : "keyN",
            KEY_O           : "keyO",
            KEY_P           : "keyP",
            KEY_Q           : "keyQ",
            KEY_R           : "keyR",
            KEY_S           : "keyS",
            KEY_T           : "keyT",
            KEY_U           : "keyU",
            KEY_V           : "keyV",
            KEY_W           : "keyW",
            KEY_X           : "keyX",
            KEY_Y           : "keyY",
            KEY_Z           : "keyZ"}

    def numericKeys(self):
        return {
            KEY_1           : "key1",
            KEY_2           : "key2",
            KEY_3           : "key3",
            KEY_4           : "key4",
            KEY_5           : "key5",
            KEY_6           : "key6",
            KEY_7           : "key7",
            KEY_8           : "key8",
            KEY_9           : "key9",
            KEY_0           : "key0"}

    def functionKeys(self):
        return {
            KEY_F1          : "keyF1",
            KEY_F2          : "keyF2",
            KEY_F3          : "keyF3",
            KEY_F4          : "keyF4",
            KEY_F5          : "keyF5",
            KEY_F6          : "keyF6",
            KEY_F7          : "keyF7",
            KEY_F8          : "keyF8",
            KEY_F9          : "keyF9",
            KEY_F10         : "keyF10",
            KEY_F11         : "keyF11",
            KEY_F12         : "keyF12"}

    def directionKeys(self):
        return {
            KEY_UP          : "keyArrowUp",
            KEY_DOWN        : "keyArrowDown",
            KEY_LEFT        : "keyArrowLeft",
            KEY_RIGHT       : "keyArrowRight"}

    def specialKeys(self):
        return {
            KEY_INSERT      : "keyInsert",
            KEY_DELETE      : "keyDelete",
            KEY_PAGEUP      : "keyPageUp",
            KEY_PAGEDOWN    : "keyPageDown",
            KEY_HOME        : "keyHome",
            KEY_END         : "keyEnd"}

    # I don't now how to name this group of keys :)
    def genericKeys(self):
        return {
            KEY_ESC         : "keyEsc",
            KEY_TAB         : "keyTab",
            KEY_CAPSLOCK    : "keyCapsLock",
            KEY_LEFTSHIFT   : "keyLeftShift",
            KEY_LEFTCTRL    : "keyLeftCtrl",
            KEY_LEFTALT     : "keyLeftAlt",
            KEY_LEFTMETA    : "keyLeftMeta",
            KEY_SPACE       : "keySpace",
            KEY_BACKSPACE   : "keyBackspace",
            KEY_ENTER       : "keyEnter",
            KEY_RIGHTSHIFT  : "keyRightShift",
            KEY_RIGHTCTRL   : "keyRightCtrl",
            KEY_RIGHTALT    : "keyRightAlt",
            KEY_RIGHTMETA   : "keyRightMeta"}

    def laptopKeys(self):
        """
        keys related for laptops
        """
        return {
            KEY_FN          : "keyFn"}
