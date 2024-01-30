from infra.adapters.response_adapter import Response
from infra.api.base_api import BaseAPI


class Login(BaseAPI):
    def __init__(self, host: str, application, token: str = None, path: str = None, ):
        super().__init__(host, application, token=token)
        self.path = path

    def get_keyboard(self) -> Response:
        """
        Gets the keyboard positions
        :return: response object
        """
        endpoint = f'{self.path}/identity/keyboard'
        response = self.get(endpoint=endpoint, headers=self.headers)
        return response

    def login(self, identifier: str, positions: list, engagement_id: str, token: str) -> Response:
        """
        Log in a user using the identifier and the keyboard positions
        :param identifier: user's phone number used for registration
        :param positions: keyboard positions obtained from the keyboard endpoint
        :param engagement_id:
        :param token:
        :return: response object
        """
        endpoint = f'{self.path}/sign-in'
        payload = {
            "identifier": identifier,
            "positions": positions,
            "engagementId": f"{engagement_id}",
            "token": f"{token}"
        }
        response = self.post(endpoint=endpoint, payload=payload, headers=self.headers)
        return response
