import requests

from jokr_library.infra.adapters.response_adapter import Response
from jokr_library.utils.logger_base import log


class BaseAPI:

    def __init__(self, host: str, application: str, token: str = None, user_id: str = None,
                 app_version: str = None):

        self.logger = log
        self.host = host
        self.token = token
        self.headers = {
            'Content-Type': 'application/json',
            'X-Platform': 'AND',
            'X-Device-Id': '438e9e341b92876a',
            'X-Device-UUID': '438e9e341b92876a',
        }
        if application:
            self.headers.update({'X-Application': application.upper()})
        if token:
            self.headers.update({'access_token': token})
        if user_id:
            self.headers.update({'X-User-Id': user_id})
        if app_version:
            self.headers.update({'X-App-Version': app_version})

    def set_token(self, new_token: str):
        self.headers.update({'access_token': new_token})

    def get(self, endpoint: str, headers: dict = None) -> Response:
        """
        Make a HTTP GET request
            :type endpoint: str
            :param endpoint: api endpoint
            :type headers: dict
            :param headers: request headers
            :type: object
            :return: Response
                """
        response = Response(requests.get(url=f'{self.host}/{endpoint}', headers=headers, timeout=10000), self.logger)
        return response

    def post(self, endpoint: str, payload: (dict, any) = None, headers: dict = None,
             content_type: str = "application/json", files: [] = None, auth: dict = None) -> Response:
        """
        Make a HTTP POST request
            :type endpoint: str
            :param endpoint: api endpoint
            :type payload: (dict | str)
            :param payload: data to be sent
            :type headers: dict
            :param headers: request headers
            :type content_type: str
            :param content_type: request Content-Type
            :type files: list
            :param files: list of files to be sent
            :type auth: dict
            :param auth: Basic authentication credentials
            :return: Response
        """
        if files is None:
            files = ()
        if content_type != "application/json" and files is not None:
            if auth is not None:
                response = Response(
                    requests.post(url=f'{self.host}/{endpoint}', data=payload, files=files, headers=headers,
                                  timeout=10000,
                                  auth=(auth["client_id"], auth["secret"])), self.logger)
            else:
                response = Response(
                    requests.post(url=f'{self.host}/{endpoint}', data=payload, files=files, headers=headers,
                                  timeout=10000), self.logger)
        else:
            response = Response(
                requests.post(url=f'{self.host}/{endpoint}', json=payload, headers=headers, timeout=10000), self.logger)

        return response

    def put(self, endpoint: str, payload: (dict, any) = None, headers: dict = None,
            content_type: str = "application/json", files: [] = None) -> Response:
        """
        Make a HTTP PUT request
            :type endpoint: str
            :param endpoint: api endpoint
            :type payload: (dict | str)
            :param payload: data to be sent
            :type headers: dict
            :param headers: request headers
            :type: object
            :return: Response
            :param content_type:
            :param files:
            :return:
        """
        if files is None:
            files = ()
        if content_type != "application/json" and files is not None:
            response = Response(
                requests.put(url=f'{self.host}/{endpoint}', data=payload, files=files, headers=headers, timeout=10000),
                self.logger)
        else:
            response = Response(
                requests.put(url=f'{self.host}/{endpoint}', json=payload, headers=headers, timeout=10000), self.logger)

        return response

    def delete(self, endpoint: str, payload: (dict | str) = None, headers: dict = None) -> Response:
        """
        Make a HTTP DELETE request
            :type endpoint: str
            :param endpoint: api endpoint
            :type payload: (dict | str)
            :param payload: data to be sent
            :type headers: dict
            :param headers: request headers
            :type: object
            :return: Response
        """
        response = Response(
            requests.delete(url=f'{self.host}/{endpoint}', json=payload, headers=headers, timeout=10000), self.logger)
        return response
