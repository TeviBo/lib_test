from infra.adapters.response_adapter import Response
from infra.api.base_api import BaseAPI


class Register(BaseAPI):
    def __init__(self, host: str, path: str = None, application: str = None, token: str = None, user_id=None) -> None:
        super().__init__(host, application, token=token, user_id=user_id)
        self.path = path
        if token:
            self.headers['Authorization'] = f'{token}'
            del self.headers['access_token']

    def generate_code(self, phone_number: int, email: str, engagement_id: str, token: str) -> Response:
        """
        Register a new user in the app.
        :param engagement_id: engagement id for registration
        :param token: token for registration
        :param phone_number: user's phone number for registration
        :param email: user email for registration
        :return: response object
        """
        endpoint = f'{self.path}/customer-register/v4/generate-code'
        if self.headers.get('X-Application') == 'JKR':
            payload = {
                "phone": phone_number,
                "email": email,
                "agoraJOKRTermCondition": True,
                "agoraJOKRPromotionsOffer": False,
                "engagementId": f"{engagement_id}",
                "token": f"{token}"
            }
        else:
            payload = {
                "phone": phone_number,
                "email": email,
                "merkaoTermCondition": True,
                "merkaoPromotionsOffer": False,
                "engagementId": f"{engagement_id}",
                "token": f"{token}"
            }
        response = self.post(endpoint=endpoint, headers=self.headers, payload=payload)
        return response

    def get_otp_code(self, phone_number: str) -> Response:
        """
        Gets the otp code sent to the user's phone
        :param phone_number: phone number of the registered user
        :return: response object
        """
        service = 'us-ux-customer-register-service'
        device_id = '438e9e341b92876a'
        endpoint = f'agora-quality/automation/otp?service={service}&identifier={phone_number},{device_id}&type=null'
        response = self.get(endpoint=endpoint, headers=self.headers)
        return response

    def validate_otp_code(self, otp_code: str) -> Response:
        """
        Validates the otp code sent to the user's phone
        :param otp_code: otp code for registered phone
        :return: response object
        """
        endpoint = f'{self.path}/customer-register/v3/validate-code'
        payload = {
            "code": otp_code
        }

        response = self.post(endpoint=endpoint, headers=self.headers, payload=payload)
        return response

    def register_user_password(self, positions: list) -> Response:
        """
        Registers the user password
        :param positions: positions obtained from the keyboard endpoint
        :return: response object
        """
        endpoint = f'{self.path}/customer-register/v3/register-user-password'
        payload = {
            "positions": positions
        }
        response = self.post(endpoint=endpoint, headers=self.headers, payload=payload)
        return response

    def register_data(self, first_name: str, last_name: str, document: str) -> Response:
        """
        Register the user data
        :param first_name: user first name
        :param last_name: user last name
        :param document: user document number
        :return: response object
        """
        endpoint = f'{self.path}/customer-profile/v7/register-data'
        payload = {
            "name": first_name,
            "lastName": last_name,
            "documentType": "DNI",
            "documentNumber": document,
            "nationality": "Peru",
            "nationalityCode": "pe"
        }

        response = self.post(endpoint=endpoint, headers=self.headers, payload=payload)
        return response
