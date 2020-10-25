from mycroft import MycroftSkill, intent_file_handler
from mycroft.messagebus.message import Message

import time
import RPi.GPIO as GPIO

BUTTON = 17

class WakeButtonRpi(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        try:
            BUTTON = self.settings.get('gpio_port', 17)
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            GPIO.add_event_detect(BUTTON, GPIO.RISING, bouncetime = 500)
        except GPIO.error:
            self.log.warning("Can't initialize GPIO - skill will not load")
            self.speak_dialog("error.initialise")
        finally:
            self.schedule_repeating_event(self.handle_button,
                                          None, 0.1, 'WakeButtonRpi')
            self.add_event('recognizer_loop:record_begin',
                           self.handle_listener_started)
            self.add_event('recognizer_loop:record_end',
                           self.handle_listener_ended)

    def handle_button(self, message):
        longpress_threshold = 2
        if GPIO.event_detected(BUTTON):
            self.log.info("GPIO.event_detected")
            pressed_time = time.time()
            while not GPIO.input(BUTTON):
                time.sleep(0.2)
            pressed_time = time.time() - pressed_time
            if pressed_time < longpress_threshold:
                self.bus.emit(Message("mycroft.mic.listen"))
            else:
                self.bus.emit(Message("mycroft.stop"))

    def handle_listener_started(self, message):
        # code to excecute when active listening begins...
        self.log.info("WakeButtonRpi listener started")

    def handle_listener_ended(self, message):
        self.log.info("WakeButtonRpi listener ended")

def create_skill():
    return WakeButtonRpi()

