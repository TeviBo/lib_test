from infra.api.login import Login
from infra.controllers.login_controller import LoginController
from infra.models.app_user_model import AppUserModel
from lib.modules import HOST, ENV_VARS
from jokr_library.utils.utils import transform_input_string


def get_keyboard(application: str) -> list[int]:
    login_client = Login(host=HOST, path=ENV_VARS[application.lower()]["paths"]["public"], application=application)
    controller = LoginController(login_client)
    keyboard = controller.get_keyboard()
    return keyboard


def login_user(user: dict, application: str) -> dict:
    login_client = Login(host=HOST, path=ENV_VARS[application.lower()]["paths"]["identity"], application=application)
    controller = LoginController(login_client)
    keyboard = get_keyboard(application)
    user["password"] = transform_input_string(user["password"], keyboard)
    controller.user = AppUserModel(**user)
    controller.login_user()
    return controller.user
