
class Result(dict):

    def __init__(self, stam='stam'):
        self.stam = stam

    def position(self):
        raise NotImplementedError()