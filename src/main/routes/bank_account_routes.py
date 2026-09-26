from flask import Blueprint, jsonify


bank_routes_bp = Blueprint("bank_routes", __name__)


@bank_routes_bp.route("/", methods=["GET"])
def hell():
    return jsonify({}), 200
