from scripts.singleton_meta import SingletonMeta


class Output(metaclass=SingletonMeta):
    def __init__(self):
        self.output_method = None

    def configure(self, output_method):
        self.output_method = output_method

    def write(self, message):
        self.output_method(message)
