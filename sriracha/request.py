class Request:
    """
    A request is sadly a class (we might take a different approach to this
    later, perhaps a dict) that represents a HTTP request.

    note: there should be a cookies method and other methods that modify something on the response, how would we go about doing that? no idea how we'll link the request and response
    """

    def __init__(self, environ):
        self.method = environ['REQUEST_METHOD']
        self.query_string = environ['QUERY_STRING']

        # apparently dict comprehasions exist!  i noticed on gunicorn
        # (hopefully same on all servers) that all headers are prefixed with
        # HTTP_ on environ
        self.headers = { key.split('HTTP_')[1] : value for key, value in environ.items() if 'HTTP_' in key }

        self.address = (environ['REMOTE_ADDR'], environ['REMOTE_PORT'])
        self.path = environ['PATH_INFO']
