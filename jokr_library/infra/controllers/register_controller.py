from infra.models.app_user_model import AppUserModel
from jokr_library.utils.data_manager.person_generator.person_factory import PersonFactory
from jokr_library.utils.logger_base import log
from jokr_library.utils.utils import transform_input_string


class RegisterController:
    _register_client = None

    def __init__(self, register_client, user: dict = None):
        self._register_client = register_client
        if not user:
            factory = (PersonFactory())
            generator = factory.get_person_generator('Peru')
            self._app_user = AppUserModel(**generator.generate_person())
        else:
            self._app_user = AppUserModel(**user)

    def change_path(self, host: str = None, path: str = None) -> None:
        if self._register_client:
            if host:
                self._register_client.host = host
                self._register_client.path = None
            if path:
                self._register_client.path = path

    @property
    def app_user(self):
        return self._app_user

    @app_user.setter
    def app_user(self, app_user):
        if isinstance(app_user, dict):
            self._app_user = AppUserModel(**app_user)
        else:
            self._app_user = app_user

    @property
    def register_client(self):
        return self._register_client

    @register_client.setter
    def register_client(self, register_client):
        self._register_client = register_client

    def generate_code(self):
        generate_code_response = None
        try:
            generate_code_response = self._register_client.generate_code(self._app_user.identifier,
                                                                         self._app_user.email,
                                                                         self._app_user.engagement_id,
                                                                         self._app_user.token)

            operation_token = generate_code_response.body["operationToken"]
            self._app_user.operation_token = operation_token
            return
        except Exception as e:
            log.error(f"Error generating code: {e}")
            raise Exception(f"Error generating code: {e}")
        except generate_code_response.status_code != 201:
            log.error(f"Error generating code.\nStatus code different than expected: {generate_code_response.body}")
            raise AssertionError(
                f"Error generating code.\nStatus code different than expected: {generate_code_response.body}")

    def get_otp_code(self, token: str):
        get_otp_code_response = None
        try:
            self._register_client.headers.update({"Authorization": f"Bearer {token}"})
            get_otp_code_response = self._register_client.get_otp_code(self._app_user.identifier)
            self._app_user.otp_code = get_otp_code_response.body["code"]
        except Exception as e:
            log.error(f"Error getting otp code: {e}")
            raise Exception(f"Error getting otp code: {e}")
        except get_otp_code_response.status_code != 200:
            log.error(f"Error getting otp code.\nStatus code different than expected: {get_otp_code_response.body}")
            raise AssertionError(
                f"Error getting otp code.\nStatus code different than expected: {get_otp_code_response.body}")

    def validate_otp_code(self):
        validate_otp_code_response = None
        try:
            self._register_client.headers.update({"Authorization": f"{self._app_user.operation_token}"})
            validate_otp_code_response = self._register_client.validate_otp_code(self._app_user.otp_code)
            self._app_user.operation_token = validate_otp_code_response.body["operationToken"]
        except Exception as e:
            log.error(f"Error validating otp code: {e}")
            raise Exception(f"Error validating otp code: {e}")
        except validate_otp_code_response.status_code != 201:
            log.error(
                f"Error validating otp code.\nStatus code different than expected: {validate_otp_code_response.body}")
            raise AssertionError(
                f"Error validating otp code.\nStatus code different than expected: {validate_otp_code_response.body}")
        return validate_otp_code_response

    def register_user_password(self, keyboard):
        register_user_password_response = None
        try:
            self._register_client.headers.update({"Authorization": f"{self._app_user.operation_token}"})
            register_user_password_response = self._register_client.register_user_password(
                transform_input_string(self._app_user.password, keyboard)
            )
            return
        except Exception as e:
            log.error(f"Error registering user password: {e}")
            raise Exception(f"Error registering user password: {e}")
        except register_user_password_response.status_code != 204:
            log.error(
                f"Error registering user password."
                f"\nStatus code different than expected: {register_user_password_response.body}")
            raise AssertionError(
                f"Error registering user password."
                f"\nStatus code different than expected: {register_user_password_response.body}")

    def register_data(self):
        register_data_response = None
        try:
            del self._register_client.headers["Authorization"]
            self._register_client.headers.update({"access_token": self._app_user.access_token})
            register_data_response = self._register_client.register_data(self._app_user.first_name,
                                                                         self._app_user.last_name,
                                                                         self._app_user.document)
            self._app_user.contact_key = register_data_response.body["contactKey"]
        except Exception as e:
            log.error(f"Error registering data: {e}")
            raise Exception(f"Error registering data: {e}")
        except register_data_response.status_code != 200:
            log.error(f"Error registering data.\nStatus code different than expected: {register_data_response.body}")
            raise AssertionError(
                f"Error registering data.\nStatus code different than expected: {register_data_response.body}")
