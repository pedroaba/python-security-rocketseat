from flask import Blueprint, jsonify, request

from src.errors.error_handler import handle_errors
from src.main.composer.balance_editor_composer import balance_editor_composer
from src.main.composer.login_creator_composer import login_creator_composer
from src.main.composer.user_register_composer import user_register_composer
from src.main.middlewares.auth_jwt import auth_jwt_verify
from src.views.http_types.http_requests import HttpRequest


bank_routes_bp = Blueprint("bank_routes", __name__)


@bank_routes_bp.route("/bank/registry", methods=["POST"])
def registry_user():
    try:
        view = user_register_composer()

        http_request = HttpRequest(body=request.json)
        response = view.handle(http_request)

        return jsonify(response.body), response.status_code
    except Exception as exception:
        return handle_errors(exception)


@bank_routes_bp.route("/bank/login", methods=["POST"])
def login_user():
    try:
        view = login_creator_composer()

        http_request = HttpRequest(body=request.json)
        response = view.handle(http_request)

        return jsonify(response.body), response.status_code
    except Exception as exception:
        return handle_errors(exception)


@bank_routes_bp.route("/bank/balance/<user_id>", methods=["PATCH"])
def balance_editor(user_id):
    try:
        token_information = auth_jwt_verify()

        view = balance_editor_composer()

        http_request = HttpRequest(
            body=request.json,
            params={"user_id": user_id},
            token_infos=token_information,
            headers=request.headers,
        )
        response = view.handle(http_request)

        return jsonify(response.body), response.status_code
    except Exception as exception:
        return handle_errors(exception)
