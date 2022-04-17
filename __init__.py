from mycroft import MycroftSkill, intent_file_handler


class Snoopy(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('snoopy.intent')
    def handle_snoopy(self, message):
        self.speak_dialog('snoopy')


def create_skill():
    return Snoopy()

