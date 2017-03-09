
# coding: utf-8
from bearlibterminal import terminal as blt
from typing import List
from functools import partial

from HealthTableau import HealthTableau
import HealthPoints
from Logger import messages, debug
import Colour
import DisplayElement
from Rectangle import Rectangle
from vec import vec
from FPSLimiter import FPSLimiter
from Game import Game

class Interface(object):
    def __init__(self) -> None:
        self.game = Game()
        messages.on_log += self.on_log
        
        blt.open()
        
        self.root = DisplayElement.DisplayDict(vec(0,0))
        
        half_width = blt.state(blt.TK_WIDTH)//2
        half_window = vec(half_width,blt.state(blt.TK_HEIGHT))
        event_log = DisplayElement.PrintArgs(
            text='', xy=vec(0,0),bbox=half_window,
            align_v=DisplayElement.TextAlignmentV.Bottom)
        self.root.elements['events'] = DisplayElement.Clickable(
            event_log, Rectangle(vec(0,0),half_window))
        
        tableau_origin = vec(half_width, 0)
        tableau_display = DisplayElement.DisplayList(tableau_origin)
        self.root.elements['tableau'] = DisplayElement.Clickable(
            tableau_display, Rectangle(tableau_origin, half_window))
        self.on_tableau_altered(self.game.hta)
    def on_tableau_altered(self, tableau):
        tableau_display = self.root.elements['tableau']
        tableau_display.element.elements.clear()
        for y, health_point in enumerate(tableau):
            point_display = DisplayElement.PrintArgs(
                health_point.summary(),vec(0,y))
            point_display_c = DisplayElement.Clickable(
                point_display, Rectangle(0,y))
            tableau_display.element.elements.append(point_display_c)
            def on_point_altered(self, point):
                self.element = self.element._replace(text=point.summary())
            health_point.after_health_change += partial(on_point_altered, point_display_c)
    def on_log(self, logger):
        events = self.root.elements['events']
        events.element = events.element._replace(text='\n'.join(
            messages.last_n(blt.state(blt.TK_HEIGHT))))
    def run(self) -> None:
        # init log
        log = []
        # draw first frame
        self.root.draw(vec(0,0))
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
                    self.root.draw(vec(0,0))
                    blt.refresh()
        blt.close()
