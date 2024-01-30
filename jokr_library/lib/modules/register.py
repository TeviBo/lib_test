import ast

from infra.api.register import Register
from infra.controllers.register_controller import RegisterController
from lib.modules import HOST, ENV_VARS
from lib.modules.login import login_user, get_keyboard
from lib.modules.oauth import basic_auth


# * /// This module contains the functions to register users /// * #


def get_otp_code(application, identifier: str) -> str:
    """
    Get the OTP code for the user
    :param application:
    :param identifier:
    :return:
    """
    oauth_access_token = basic_auth(ENV_VARS[application.lower()]["oauth_credentials"]["register"])
    register_client = Register(host=HOST)
    controller = RegisterController(register_client)
    controller.app_user.identifier = identifier
    controller.get_otp_code(oauth_access_token)
    return controller.app_user.otp_code


def register_random_user(application: str) -> dict:
    """
    Register a random user
    :param application: Application where the user will be registered. Eg: JKR/MRK
    :return: AppUserModel
    """
    register_client = Register(host=HOST, path=ENV_VARS[application.lower()]["paths"]["public"],
                               application=application)
    controller = RegisterController(register_client)

    # * 1. Generate code
    controller.app_user.engagement_id = ENV_VARS[application.lower()]["register_tokens"]["engagementId"]
    controller.app_user.token = ENV_VARS[application.lower()]["register_tokens"]["token"]
    controller.generate_code()

    # * 3. Get OTP code
    controller.app_user.otp_code = get_otp_code(application, controller.app_user.identifier)

    # * 4. Validate OTP code
    controller.change_path(path=ENV_VARS[application.lower()]["paths"]["public"])
    controller.validate_otp_code()

    # * 5. Get keyboard
    keyboard = get_keyboard(application)

    # * 6. Register user password
    controller.register_user_password(keyboard)

    # * 7. Login
    controller.app_user = login_user(ast.literal_eval(controller.app_user.__str__()), application)

    # * 8. Register data
    controller.change_path(path=ENV_VARS[application.lower()]["paths"]["private"])
    controller.register_data()

    # * 9. Return user data
    return ast.literal_eval(controller.app_user.__str__())
