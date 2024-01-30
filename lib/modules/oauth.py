from infra.api.oauth import OAuth
from infra.controllers.oauth_controller import OAuthController
from lib.modules import HOST


def basic_auth(credentials) -> str:
    """
    Gets the access token for the API
    :type: object
    :return: auth data
    """
    oauth_client = OAuth(HOST)
    oauth_client.token = credentials
    oauth_controller = OAuthController(oauth_client)
    oauth_controller.get_access_token_for_otp()
    return oauth_controller.user.access_token
