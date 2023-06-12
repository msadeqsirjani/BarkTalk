import os
from gtts import gTTS
from uuid import uuid4
from config import MEDIA_DIR


def convert(text: str, language: str = 'en') -> str:
    tts = gTTS(text=text,
               lang=language)

    exact_file_name = f"{str(uuid4())}.wav"
    exact_file_path = os.path.join(MEDIA_DIR, exact_file_name)
    tts.save(savefile=exact_file_path)

    return exact_file_name
