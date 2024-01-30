class OAuthUser:
    def __init__(self, **oauth_user_data):
        self._secret = oauth_user_data.get('secret')
        self._client_id = oauth_user_data.get('client_id')
        self._access_token = oauth_user_data.get('token')

    def __str__(self):
        return {"client_id": self._client_id, "secret": self._secret}

    @property
    def client_id(self):
        return self._client_id

    @property
    def secret(self):
        return self._secret

    @property
    def access_token(self):
        return self._access_token

    @client_id.setter
    def client_id(self, value):
        self._client_id = value

    @secret.setter
    def secret(self, value):
        self._secret = value

    @access_token.setter
    def access_token(self, value):
        self._access_token = value
