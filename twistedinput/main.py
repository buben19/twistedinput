#!/usr/bin/env python
from __future__ import unicode_literals
from twisted.internet import reactor
from device import EventDevice
from protocol import EventProtocol
from factory import InputEventFactory
from mapping import GamepadEventMapping


class GamepadProtocol(EventProtocol):

    def button1(self, event):
        print "button 1:", event

    def button2(self, event):
        print "button 2:", event

    def button3(self, event):
        print "button 3:", event

    def button4(self, event):
        print "button 4:", event

    def triggerLeft1(self, event):
        print "trigger left 1:", event

    def triggerRight1(self, event):
        print "trigger right 1:", event

    def triggerLeft2(self, event):
        print "trigget left 2:", event

    def triggerRight2(self, event):
        print "trigger right 2:", event

    def joystickLeftX(self, event):
        print "joystick left X:", event

    def joystickLeftY(self, event):
        print "joystick left Y", event

    def joystickRightX(self, event):
        print "joystick right X:", event

    def joystickRightY(self, event):
        print "joystick right Y:", event

    def dpadX(self, event):
        print "dpad X:", event

    def dpadY(self, event):
        print "dpad Y:", event

    def button9(self, event):
        print "button 9:", event

    def button10(self, event):
        print "button 10:", event

    def buttonJoystickLeft(self, event):
        print "button joystick left:", event

    def buttonJoystickRight(self, event):
        print "button joystick right:", event

EventDevice(
    GamepadProtocol(
        InputEventFactory(),
        GamepadEventMapping()),
    "/dev/input/event13").startReading()
reactor.run()
