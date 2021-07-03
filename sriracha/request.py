class Request:
    """
    A request is sadly a class (we might take a different approach to this
    later, perhaps a dict) that represents a HTTP request.
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
        
        self.response_headers = []
        self.response_cookies = []

    def header(header, value):
        """
        sets a response header 
        """

        self.response_headers.append((header, value))

    def cookie(cookie, value):
        """
        sets a cookie
        """

        self.response_cookies.append((cookie, value))
