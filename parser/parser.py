__author__ = 'Oleg Gromyak'


class Parser:
    def __init__(self, code=None):
        self.code = code
        self.current = 0  # current position
        if self.code:
            self.proceed()

    def proceed(self, code=None):
        self.code = self.code or code
        self.current = 0
        if not self.code:
            return None
