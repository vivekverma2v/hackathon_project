
from converter.text_to_speech import TextToSpeech
from logger.logger import exc_logger, logger



class Main:

    def __init__(self):
        self.logger = logger       


    @staticmethod
    def getInstance():
        """ Static method to fetch the current instance. """
        return Main()

    def text_to_speech(self, uName, text, language):
        return TextToSpeech(self).text_to_speech(uName, text, language)

    def speech_to_text(self, uName, language):
        return TextToSpeech(self).record_voice(uName, language)