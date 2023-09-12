import io
import os
import base64
from uuid import uuid4
from config import MEDIA_DIR, ALLOWED_LANGUAGES
from utilities.file_extensions import allowed_file, get_file_extension
from flask import Flask, send_file, jsonify, request, url_for
from werkzeug.utils import secure_filename
from voice_engine import speech_to_text, text_to_speech
from brain_engine import gpt_engine

app = Flask(__name__)


@app.route("/download/<file_name>")
def download(file_name: str):
    file_path = os.path.join(MEDIA_DIR, file_name)
    if not os.path.exists(file_path):
        return jsonify({"data": None,
                        "message": "There is no file with this name",
                        "status": "error"}), 404

    return_data = io.BytesIO()
    with open(file_path, 'rb') as file:
        return_data.write(file.read())

    return_data.seek(0)

    # os.remove(file_path)

    return send_file(path_or_file=return_data,
                     download_name=file_name,
                     mimetype='audio/wav',
                     as_attachment=True)

    # return send_file(path_or_file=file_path, as_attachment=True)


@app.route("/supported_language")
def supported_language():
    return jsonify({"data": ALLOWED_LANGUAGES,
                    "message": None,
                    "status": "success"}), 200


@app.route("/ask/<language>", methods=["POST"])
def ask(language: str):
    for file_key, file in request.files.items():
        if file.filename == "":
            return jsonify({"data": None,
                            "message": "No selected file is available",
                            "status": "error"}), 400

        if file and allowed_file(file.filename):
            secure_file_name = secure_filename(file.filename)
            secure_file_extension = get_file_extension(file_name=secure_file_name)
            secure_file_path = os.path.join(MEDIA_DIR, f"{str(uuid4())}{secure_file_extension}")
            file.save(secure_file_path)

            prompt = speech_to_text.convert(file_path=secure_file_path,
                                            language=language)

            if prompt is None:
                return jsonify({"data": None,
                                "message": "Google Speech Recognition could not understand audio",
                                "status": "success"}), 400

            os.remove(secure_file_path)

            engine = gpt_engine.GptEngine()

            answer_text = engine.command(prompt=prompt)

            exact_answer_voice_name = text_to_speech.convert(text=answer_text,
                                                             language=language)

            data = {
                "prompt": prompt,
                "prompt_language": language,
                "answer": {
                    "text": answer_text,
                    "file_name": exact_answer_voice_name,
                    "answer_language": language,
                    "voice_path": url_for("download", file_name=exact_answer_voice_name, _external=True,
                                          _scheme="http")
                }
            }

            return jsonify({"data": data,
                            "message": None,
                            "status": "success"}), 200
        else:
            return jsonify({"data": None,
                            "message": "File type not allowed. Only mp3 and wav files are acceptable",
                            "status": "error"}), 400
    return jsonify({"data": None,
                    "message": "No file part is available",
                    "status": "error"}), 400


@app.route("/ask/web/<language>", methods=["POST"])
def ask_web(language: str):
    data = request.get_json()
    
    file_name = data['file_name']
    file_content = data['file_content']

    if file_name == "":
        return jsonify({"data": None,
                        "message": "No selected file is available",
                        "status": "error"}), 400    
    
    if file_name and file_content and allowed_file(file_name=file_name):
        secure_file_name = secure_filename(file_name)
        secure_file_extension = get_file_extension(file_name=secure_file_name)
        secure_file_path = os.path.join(MEDIA_DIR, f"{str(uuid4())}{secure_file_extension}")

        print(secure_file_path)

        with open(secure_file_path, 'wb') as file:
            file.write(base64.b64decode(file_content))

        prompt = speech_to_text.convert(file_path=secure_file_path,
                                        language=language)

        if prompt is None:
            return jsonify({"data": None,
                            "message": "Google Speech Recognition could not understand audio",
                            "status": "success"}), 400

        os.remove(secure_file_path)

        engine = gpt_engine.GptEngine()

        answer_text = engine.command(prompt=prompt)

        exact_answer_voice_name = text_to_speech.convert(text=answer_text,
                                                        language=language)

        data = {
                "prompt": prompt,
                "prompt_language": language,
                "answer": {
                    "text": answer_text,
                    "file_name": exact_answer_voice_name,
                    "answer_language": language,
                    "voice_path": url_for("download", file_name=exact_answer_voice_name, _external=True, _scheme="http")
                }
            }   

        return jsonify({"data": data,
                        "message": None,
                        "status": "success"}), 200    

        # return jsonify({"data": None,
        #                 "message": "DONE",
        #                 "status": "success"}), 200
    else:
        return jsonify({"data": None,
                        "message": "File type not allowed. Only mp3 and wav files are acceptable",
                        "status": "error"}), 400

if __name__ == '__main__':
    app.run()
