from flask import Blueprint, jsonify, request

from src.main.composer.login_creator_composer import login_creator_composer
from src.main.composer.user_register_composer import user_register_composer
from src.views.http_types.http_requests import HttpRequest


bank_routes_bp = Blueprint("bank_routes", __name__)


@bank_routes_bp.route("/bank/registry", methods=["POST"])
def registry_user():
    view = user_register_composer()

    http_request = HttpRequest(body=request.json)
    response = view.handle(http_request)

    return jsonify(response.body), response.status_code


@bank_routes_bp.route("/bank/login", methods=["POST"])
def login_user():
    view = login_creator_composer()

    http_request = HttpRequest(body=request.json)
    response = view.handle(http_request)

    return jsonify(response.body), response.status_code


@bank_routes_bp.route("/bank/balance/<user_id>", methods=["PATCH"])
def balance_editor(user_id):
    view = user_register_composer()

    http_request = HttpRequest(body=request.json, params={"user_id": user_id})
    response = view.handle(http_request)

    return jsonify(response.body), response.status_code
