from types import ModuleType
from . import utils
from .request import Request

class Application:
    """
    an application is an application.

    note: only one application can be created per runtime! (this is not very
    strict, i'm not gonna tell your parents, it's just gonna fuck up)
    """

    def __init__(self, settings_module: ModuleType):
        # hacky way to get all variables that are not weird python variables
        self.settings = {key: value for key, value in vars(settings_module).items() if not key in utils.IGNORE_VARS}

    def __call__(self, environ, start_response):
        """
        per WSGI, this method is called on every request
        """

        request = Request(environ)

        print(request)
