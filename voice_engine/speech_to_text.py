import os
import config
import speech_recognition as sr


def convert(file_path: str, language: str = 'en-US') -> str:
    recognizer = sr.Recognizer()

    with sr.AudioFile(file_path) as src:
        audio_data = recognizer.record(src)

    try:
        text = recognizer.recognize_google(audio_data=audio_data,
                                           language=language)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
