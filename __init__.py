from mycroft import MycroftSkill, intent_file_handler


class Terminal(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('terminal.intent')
    def handle_terminal(self, message):
        self.speak_dialog('terminal')


def create_skill():
    return Terminal()

