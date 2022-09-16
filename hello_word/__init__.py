# Simple project that print hello-world

class HelloWorld:
    __version__ = "0.0.0"

    def __init__(self, message):
        self.message = message

    def log(self):
        print(self.message)
        return self.message
