import os
from gtts import gTTS
from uuid import uuid4
from config import MEDIA_DIR
from voice_engine.mp3_to_other_type import convert as wav_convertor


def convert(text: str, language: str = 'en') -> str:
    tts = gTTS(text=text,
               lang=language)

    exact_file_name = f"{str(uuid4())}.mp3"
    exact_file_path = os.path.join(MEDIA_DIR, exact_file_name)
    tts.save(savefile=exact_file_path)
    file_path = wav_convertor(audio_path=exact_file_path)

    os.remove(exact_file_path)

    return exact_file_name.replace(".mp3", ".wav"), file_path
