from googletrans import Translator


def translate(text: str, language: str) -> str:
    translator = Translator()
    translated_response = translator.translate(text=text,
                                               dest=language)
    return translated_response.text
