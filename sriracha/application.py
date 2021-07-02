from types import ModuleType

class Application:

    def __init__(self, settings_module: ModuleType):
        # hacky way to get all variables that are not weird python variables
        self.settings = [(key, value) for key, value in vars(settings_module).keys() if not key in utils.IGNORE_VARS]
