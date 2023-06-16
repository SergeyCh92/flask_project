from flask import Blueprint, abort, g, jsonify, request, send_file

from web_service.authentication import auth
from web_service.utils import (
    check_file_ownership,
    delete_file_from_store,
    get_file_data,
    get_file_hash,
    record_data_file_ownership,
    save_file_to_folder,
)

files_api = Blueprint("files_api", __name__)


@files_api.route("/upload", methods=["POST"])
@auth.login_required
def upload_file():
    file = request.data
    file_hash = get_file_hash(file)
    save_file_to_folder(file, file_hash)
    record_data_file_ownership(g.flask_httpauth_user, file_hash)
    return jsonify({"file_hash": file_hash})


@files_api.route("/download", methods=["GET"])
def download_file():
    file_hash = request.args.get("file_hash")
    file_data = get_file_data(file_hash)
    if not file_data:
        abort(404, "The file with the specified name is missing in the store.")
    return send_file(file_data, download_name=file_hash, as_attachment=True)


@files_api.route("/delete", methods=["DELETE"])
@auth.login_required
def delete_file():
    file_hash = request.args.get("file_hash")
    is_owner = check_file_ownership(g.flask_httpauth_user, file_hash)
    if not is_owner:
        abort(404, "You don't have any files with the specified name.")
    delete_file_from_store(file_hash)
    return jsonify({"success": True})
