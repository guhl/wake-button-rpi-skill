from mycroft import MycroftSkill, intent_file_handler


class WakeButtonRpi(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('rpi.button.wake.intent')
    def handle_rpi_button_wake(self, message):
        self.speak_dialog('rpi.button.wake')


def create_skill():
    return WakeButtonRpi()

