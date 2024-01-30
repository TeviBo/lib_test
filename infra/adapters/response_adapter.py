import json

from utils.logger_base import log_data


class Response:
    def __init__(self, response, logger, log_status_codes=None):
        self.status_code = response.status_code
        avoided_status_codes = [204, 401, 403, 404, 405]
        if response.status_code <= 500 and response.status_code not in avoided_status_codes:
            self.body = json.loads(response.text)
        else:
            self.body = response.text
        self.method = response.request.method
        self.endpoint = response.url
        self.request = response.request.body
        self.headers = response.request.headers
        if log_status_codes is None:
            log_status_codes = [200, 201, 204]
        if self.status_code not in log_status_codes:
            log_message = (
                "\n****************************\n"
                "////////////////////////////\n"
                "****************************\n"
                "|     [Request Data]       |\n"
                "****************************\n"
                f"[Endpoint]: {self.endpoint}\n"
                f"[Method]: {self.method}\n"
                f"[Headers]: {self.headers}\n"
                f"[Request Payload]: {self.request}\n"
                "****************************\n"
                "////////////////////////////\n"
                "****************************\n"
                "|     [Response Data]       |\n"
                "****************************\n"
                f"[Status Code]: {self.status_code}\n"
                f"[Response Body]: \n{self.body}\n"
                "****************************\n"
                "///////////////////////////\n"
                "****************************\n"
            )
            log_data(logger, log_message)
