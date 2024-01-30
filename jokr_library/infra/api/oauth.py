from jokr_library.infra.adapters.response_adapter import Response
from jokr_library.infra.api.base_api import BaseAPI


class OAuth(BaseAPI):
    def __init__(self, host, application=None, token=None):
        super().__init__(host, application)
        self.token = token if not None else None

    def basic_auth(self) -> Response:
        """
        Gets the access token for the API
        :type: object
        :return: Response
        """
        endpoint = f"oauth/access-token"
        self.headers.update(
            {'Host': 'api-qa.agora.pe', 'Content-Length': '29', 'Content-Type': 'application/x-www-form-urlencoded'})
        payload = 'grant_type=client_credentials'

        response = self.post(endpoint=endpoint, payload=payload, headers=self.headers, auth=self.token,
                             content_type="application/x-www-form-urlencoded")
        return response
