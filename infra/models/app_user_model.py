from utils.data_manager.person_generator.person_types.person import Person


class AppUserModel:
    def __init__(self, **person: Person):
        self._user = person

    def __str__(self):
        return str(self._user)

    @property
    def identifier(self):
        return self._user.get('phone', None)

    @property
    def password(self):
        return self._user.get('password', None)

    @property
    def email(self):
        return self._user.get('email', None)

    @property
    def first_name(self):
        return self._user.get('first_name', None)

    @property
    def last_name(self):
        return self._user.get('last_name', None)

    @property
    def document(self):
        return self._user.get('document', None)

    @property
    def doc_type(self):
        return self._user.get('doc_type', None)

    @property
    def nationality_code(self):
        return self._user.get('nationality_code', None)

    @property
    def access_token(self):
        return self._user.get('access_token', None)

    @property
    def operation_token(self):
        return self._user.get('operation_token', None)

    @property
    def engagement_id(self):
        return self._user.get('engagement_id', None)

    @property
    def token(self):
        return self._user.get('token', None)

    @property
    def user_id(self):
        return self._user.get('user_id', None)

    @property
    def app_version(self):
        return self._user.get('app_version', None)

    @property
    def otp_code(self):
        return self._user.get('otp_code', None)

    @property
    def contact_key(self):
        return self._user.get('contact_key', None)

    @identifier.setter
    def identifier(self, value):
        self._user['phone'] = value

    @password.setter
    def password(self, value):
        self._user['password'] = value

    @email.setter
    def email(self, value):
        self._user['email'] = value

    @first_name.setter
    def first_name(self, value):
        self._user['first_name'] = value

    @last_name.setter
    def last_name(self, value):
        self._user['last_name'] = value

    @document.setter
    def document(self, value):
        self._user['document'] = value

    @doc_type.setter
    def doc_type(self, value):
        self._user['doc_type'] = value

    @nationality_code.setter
    def nationality_code(self, value):
        self._user["nationality_code"] = value

    @access_token.setter
    def access_token(self, value):
        self._user["access_token"] = value

    @operation_token.setter
    def operation_token(self, value):
        self._user["operation_token"] = value

    @engagement_id.setter
    def engagement_id(self, value):
        self._user["engagement_id"] = value

    @token.setter
    def token(self, value):
        self._user["token"] = value

    @user_id.setter
    def user_id(self, value):
        self._user["user_id"] = value

    @app_version.setter
    def app_version(self, value):
        self._user["app_version"] = value

    @otp_code.setter
    def otp_code(self, value):
        self._user["otp_code"] = value

    @contact_key.setter
    def contact_key(self, value):
        self._user["contact_key"] = value
