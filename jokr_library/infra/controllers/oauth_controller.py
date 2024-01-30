from infra.models.oauth_user_model import OAuthUser
from jokr_library.utils.logger_base import log


class OAuthController:
    def __init__(self, oauth_client):
        self._oauth_client = oauth_client
        self._oauth_user = OAuthUser()

    @property
    def user(self):
        return self._oauth_user

    def get_access_token_for_otp(self):
        get_access_token_response = None
        try:
            get_access_token_response = self._oauth_client.basic_auth()
            self._oauth_user.access_token = get_access_token_response.body["access_token"]
            log.debug(f"OAuth token: {self._oauth_user.access_token}")
        except Exception as e:
            log.error(f"Error getting access token: {e}")
            raise Exception(f"Error getting access token: {e}")
        except get_access_token_response.status_code != 200:
            log.error(
                f"Error getting access token.\nStatus code different than expected: {get_access_token_response.body}")
            raise AssertionError(
                f"Error getting access token.\nStatus code different than expected: {get_access_token_response.body}")
