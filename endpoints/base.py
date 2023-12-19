import requests


class BaseAPI:

    def __init__(self, session: requests.Session, url: str):
        self.session = session
        self.url = url

    def get(self, *args, **kwargs):
        response = self.session.get(*args, **kwargs)
        return response
