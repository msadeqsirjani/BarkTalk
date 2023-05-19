import os
from config import ALLOWED_EXTENSIONS


def allowed_file(file_name: str) -> bool:
    file_extension = get_file_extension(file_name=file_name)
    return '.' in file_name and file_extension in ALLOWED_EXTENSIONS


def get_file_extension(file_name: str) -> str:
    return os.path.splitext(file_name)[1]


def get_file_name(file_name: str) -> str:
    return os.path.splitext(file_name)[0]
