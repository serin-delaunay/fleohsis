
# coding: utf-8
from bearlibterminal import terminal as blt
from typing import List

from HealthTableau import HealthTableau
import HealthPoints
import Colour
import DisplayElement
from Rectangle import Rectangle
from vec import ivec
from FPSLimiter import FPSLimiter
from Game import Game

class Interface(object):
    def __init__(self) -> None:
        blt.open()
        self.root = DisplayElement.DisplayDict(ivec(0,0))
        half_width = blt.state(blt.TK_WIDTH)//2
        half_window = ivec(half_width,blt.state(blt.TK_HEIGHT))
        event_log = DisplayElement.PrintArgs(text='', xy=ivec(0,0),bbox=half_window,align_v=DisplayElement.TextAlignmentV.Bottom)
        self.root.elements['events'] = DisplayElement.Clickable(event_log, Rectangle(ivec(0,0),half_window))
        self.game = Game()
        self.game.on_log += self.on_log
        # TODO set self.root.tableau
    def on_log(self, game):
        events = self.root.elements['events']
        events.element = events.element._replace(text='\n'.join(self.game.log_lines))
    def run(self) -> None:
        # init log
        log = []
        # draw first frame
        self.root.draw(ivec(0,0))
        fps_limiter = FPSLimiter()
        blt.set('window:title="FLEOHSIS ({0} FPS)"'.format(fps_limiter.get_fps()))
        blt.refresh()
        # read-advance-display loop
        stop = False
        while not stop:
            fps_limiter.wait()
            blt.set('window:title="FLEOHSIS ({0} FPS)"'.format(fps_limiter.get_fps()))
            while blt.has_input():
                if blt.read() == blt.TK_CLOSE:
                    stop = True
                else:
                    self.game.advance()
                    blt.clear()
                    self.root.draw(ivec(0,0))
                    blt.refresh()
        blt.close()
