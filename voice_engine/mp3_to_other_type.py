from pydub import AudioSegment


def convert(audio_path: str, file_format: str = 'wav'):
    audio = AudioSegment.from_mp3(audio_path)
    audio_path = audio_path.replace(".mp3", f".{file_format}")
    audio.export(audio_path, format=file_format)

    return audio_path
