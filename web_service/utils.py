import hashlib
import io
import json
import logging
import os
import shutil

from web_service.constants import STORAGE_NAME


def save_file(path: str, data: bytes):
    with open(path, "wb") as file:
        file.write(data)


def get_file_hash(data: bytes) -> str:
    file_hash = hashlib.sha256()
    file_hash.update(data)
    return file_hash.hexdigest()


def save_file_to_folder(data: bytes, file_hash: str):
    dir_name = file_hash[:2]
    if not os.path.exists(f"{STORAGE_NAME}/{dir_name}"):
        os.mkdir(f"{STORAGE_NAME}/{dir_name}")
    save_file(f"{STORAGE_NAME}/{dir_name}/{file_hash}", data)
    logging.info(f"the file has been successfully saved to the {STORAGE_NAME}/{dir_name} folder")


def get_file_data(file_name: str) -> None | io.BytesIO:
    for path, dirs, file_names in os.walk(STORAGE_NAME):
        if file_name not in file_names:
            continue
        with open(f"{path}/{file_name}", "rb") as file:
            return io.BytesIO(file.read())


def record_data_file_ownership(username: str, file_hash: str):
    with open(f"{STORAGE_NAME}/files_ownerships.txt", "r+") as fp:
        files_ownerships = json.load(fp)
        if files_ownerships.get(username):
            files_ownerships[username].append(file_hash)
        else:
            files_ownerships[username] = [file_hash]
        fp.seek(0)
        json.dump(files_ownerships, fp)
        fp.truncate()


def check_file_ownership(username: str, file_hash: str) -> bool:
    result = False
    with open(f"{STORAGE_NAME}/files_ownerships.txt", "r+") as file:
        files_ownerships = json.load(file)
        if files_ownerships.get(username) and file_hash in files_ownerships.get(username):
            files_ownerships[username] = [item for item in files_ownerships[username] if item != file_hash]
            file.seek(0)
            json.dump(files_ownerships, file)
            file.truncate()
            result = True
    return result


def delete_file_from_store(file_name: str):
    for path, dirs, file_names in os.walk(STORAGE_NAME):
        if file_name not in file_names:
            continue
        shutil.rmtree(path)
        break
