from machine import Pin
import time


class Light:
    def __init__(self, delay, button, led):
        self.delay = delay
        self.button = Pin(button, Pin.IN, Pin.PULL_UP)
        self.led = Pin(led, Pin.OUT)
        self.state = self.off

    def execute(self):
        self.state()

    def off(self):
        self.led.off()
        time.sleep(self.delay)

        if self.button.value() == 0:
            self.state = self.onw
        else:
            self.state = self.off

    def onw(self):
        self.led.on()
        time.sleep(self.delay)

        if self.button.value() == 1:
            self.state = self.on
        else:
            self.state = self.onw

    def on(self):
        self.led.on()
        time.sleep(self.delay)

        if self.button.value() == 1:
            self.state = self.on
        else:
            self.state = self.offw

    def offw(self):
        self.led.off()
        time.sleep(self.delay)

        if self.button.value() == 1:
            self.state = self.off
        else:
            self.state = self.offw


# SW2 (Pin id: 7) for button and LED3 (Pin id: 20) for lamp.
# Clock frequency of the state machine is 20 Hz (50 ms period)

control = Light(0.05, 7, 20)

while True:
    control.execute()