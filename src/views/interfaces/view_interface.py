from abc import ABC, abstractmethod

from src.views.http_types.http_requests import HttpRequest
from src.views.http_types.http_response import HttpResponse


class ViewInterface(ABC):
    @abstractmethod
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        raise NotImplementedError()
