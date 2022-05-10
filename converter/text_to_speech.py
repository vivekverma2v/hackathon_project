
# Import the required module for text 
# to speech conversion
import os
from io import BytesIO

from constant.constant import Constant
from gtts import gTTS
import speech_recognition as sr

class TextToSpeech:

    def __init__(self, mainObj) -> None:
        self.obj = mainObj

    def text_to_speech(self, uName, mytext, language):
        # Passing the text and language to the engine, 
        # here we have marked slow=False. Which tells 
        # the module that the converted audio should 
        # have a high speed
        myobj = gTTS(text = mytext, lang = language, slow = False)

        path = Constant.AUDIO_PATH.format(uName)
        
        # Check whether the specified path exists or not
        isExist = os.path.exists(path)

        if not isExist:  
            # Create a new directory because it does not exist 
            os.makedirs(path)
            self.obj.logger.info("The new directory is created!")

        # Saving the converted audio in a mp3 file named
        # welcome
        save_path = os.path.join(path, Constant.VOICE_NAME)
        myobj.save(save_path)

        # Playing the converted file
        # self.__playsound(myobj)
        return save_path

    def record_voice(self, uName, language = 'en-IN'):
        while True:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio=r.listen(source)
                try:    
                    text = r.recognize_google(audio, language="en-IN")
                except Exception as e:
                    self.obj.logger.error(str(e))
                    pass

                return self.text_to_speech(uName, text, language)

    def __playsound(slef, tts):
        # convert to file-like object
        fp = BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)

        from mpg123 import Mpg123, Out123
        mp3 = Mpg123()
        mp3.feed(fp.read())
        out = Out123()

        for frame in mp3.iter_frames(out.start):
            out.play(frame)