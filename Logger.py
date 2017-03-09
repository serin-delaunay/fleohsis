
# coding: utf-8
from obsub import event

class Logger(object):
    def __init__(self):
        self._log = []
    def log(self, message):
        self._log.append(message)
        self.on_log()
    @event
    def on_log(self): pass
    def last_n(self, n):
        return self._log[-n:]

messages = Logger()
debug = Logger()

debug.on_log += lambda logger : print(logger.last_n(1)[0])
