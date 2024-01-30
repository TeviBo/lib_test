from utils.logger_base import log


class LoginController:
    def __init__(self, login_client, user=None):
        self._login_client = login_client
        self._user = user

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user

    def get_keyboard(self):
        get_keyboard_response = None
        try:
            get_keyboard_response = self._login_client.get_keyboard()
        except Exception as e:
            log.error(f"Error getting keyboard: {e}")
            raise AssertionError(f"Error getting keyboard: {e}")
        except get_keyboard_response.status_code != 200:
            log.error(f"Error getting keyboard.\nStatus code different than expected: {get_keyboard_response.body}")
            raise AssertionError(
                f"Error getting keyboard.\nStatus code different than expected: {get_keyboard_response.body}")
        return get_keyboard_response.body["keyboard"]

    def login_user(self):
        login_response = None
        try:
            login_response = self._login_client.login(self._user.identifier, self._user.password,
                                                      self._user.engagement_id, self._user.token)
            self._user.access_token = login_response.body["access_token"]
            self._user.operation_token = login_response.body["operationToken"]
            self._user.user_id = login_response.body["userId"]

        except Exception as e:
            log.error(f"Error logging in: {e}")
            raise AssertionError(f"Error logging in: {e}")
        except login_response.status_code != 201:
            log.error(f"Error logging in.\nStatus code different than expected: {login_response.body}")
            raise AssertionError(f"Error logging in.\nStatus code different than expected: {login_response.body}")
