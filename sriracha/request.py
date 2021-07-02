class Request:
    """
    A request is sadly a class (we might take a different approach to this
    later, perhaps a dict) that represents a HTTP request.

    note: there should be a cookies method and other methods that modify something on the response, how would we go about doing that? no idea how we'll link the request and response
    """

    def __init__(self, address, path, headers):
        self.address = address
        self.path = path
        self.headers = headers
