# BarkTalk: ChatGPT-powered Voice Assistant

[![GitHub license](https://img.shields.io/github/license/msadeqsirjani/BarkTalk)](https://github.com/msadeqsirjani/BarkTalk/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/msadeqsirjani/BarkTalk)](https://github.com/msadeqsirjani/BarkTalk/issues)
[![GitHub stars](https://img.shields.io/github/stars/msadeqsirjani/BarkTalk)](https://github.com/msadeqsirjani/BarkTalk/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/msadeqsirjani/BarkTalk)](https://github.com/msadeqsirjani/BarkTalk/network)

BarkTalk is a ChatGPT-powered voice assistant that uses Google Text-to-Speech (TTS) and Speech-to-Text (STT) to enable natural language conversation with users in multiple languages. The app is written in Python and runs on your local machine or server. You can use BarkTalk to perform various tasks, such as playing music, searching the web, getting the weather forecast, setting reminders, and more. 

## Installation

To use BarkTalk, you'll need to follow these steps:

1. Clone this repository to your local machine.
2. Install the required Python packages by running `pip install -r requirements.txt`.
3. Create a Google Cloud account and enable the Text-to-Speech and Speech-to-Text APIs.
4. Set up authentication by creating a service account key and exporting the key as an environment variable: `export GOOGLE_APPLICATION_CREDENTIALS="/path/to/key.json"`.
5. Run `python barktalk.py` to start the voice assistant.

## Usage

Once you've installed and set up BarkTalk, you can use it by speaking to it in natural language. Here are some examples of what you can do:

- "What's the weather like today?"
- "Play some music by Adele."
- "Search for the best pizza places near me."
- "Set a reminder for 3 PM to call Mom."

BarkTalk supports multiple languages, so you can speak to it in any language that Google TTS and STT support. To change the language, modify the `LANGUAGE_CODE` variable in `barktalk.py`.

## Contributing

If you'd like to contribute to BarkTalk, please follow these guidelines:

1. Fork thisrepository and clone it to your local machine.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test them thoroughly.
4. Write tests for your changes and make sure they pass.
5. Submit a pull request with a clear description of your changes and why they're necessary.

## License

BarkTalk is licensed under the MIT License. See `LICENSE` for more information.

## Credits

BarkTalk was created by [msadeqsirjani](https://github.com/msadeqsirjani) using the following libraries and APIs:

- [Google Text-to-Speech API](https://cloud.google.com/text-to-speech)
- [Google Speech-to-Text API](https://cloud.google.com/speech-to-text)
- [ChatGPT](https://huggingface.co/transformers/model_doc/gpt.html)
- [pydub](http://pydub.com/)
- [SpeechRecognition](https://github.com/Uberi/speech_recognition)
- [pyaudio](https://people.csail.mit.edu/hubert/pyaudio/)

## Contact

If you have any questions or feedback about BarkTalk, please feel free to contact me at [msadeqsirjani@gmail.com](mailto:m.sadeq.sirjani@gmail.com).