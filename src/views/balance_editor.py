from typing import Any
from src.controllers.interfaces.balance_editor import BalanceEditorInterface
from src.views.http_types.http_requests import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface


class BalanceEditorView(ViewInterface):
    def __init__(self, controller: BalanceEditorInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        user_id = http_request.params.get("user_id")
        new_balance = http_request.body.get("new_balance")
        header_user_id = http_request.headers.get("uid")

        self.__validate_inputs(new_balance, user_id, header_user_id)
        response = self.__controller.edit(user_id, new_balance)
        return HttpResponse({"data": response}, status_code=200)

    def __validate_inputs(
        self, new_balance: Any, user_id: Any, header_user_id: Any
    ) -> None:
        if (
            not new_balance
            or not user_id
            or not isinstance(new_balance, float)
            or not isinstance(user_id, str)
            or (int(header_user_id) != int(user_id))
        ):
            raise Exception("Invalid input")
