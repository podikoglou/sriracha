class Controller:

    def __init__(self):
        if not 'handle_request' in dir(self):
            # we create a new handle_request that returns with error code 500
            # and a user-friendly page saying "500"
            self.handle_request = handle_request_err(500)
