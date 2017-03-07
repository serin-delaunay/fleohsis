
# coding: utf-8
from bearlibterminal import terminal as blt
from typing import List

#%load_ext autoreload

from HealthTableau import HealthTableau
import HealthPoints
import Colour
import DisplayElement
from Rectangle import Rectangle
from vec import ivec
from FPSLimiter import FPSLimiter

#%autoreload 2

class Interface(object):
    def __init__(self) -> None:
        self.root = DisplayElement.DisplayDict(ivec(0,0))
        half_width = blt.state(blt.TK_WIDTH)//2
        half_window = ivec(half_width,blt.state(blt.TK_HEIGHT))
        event_log = DisplayElement.PrintArgs('', ivec(0,0),half_window)
        self.root.elements['events'] = DisplayElement.Clickable(event_log, Rectangle(ivec(0,0),half_window))
        # TODO set self.root.tableau
    def update_log(self, lines : List[str]):
        events = self.root.elements['events']
        events.element = events.element._replace(text='\n'.join(lines))
    def run(self) -> None:
        # init health
        ht = HealthTableau()
        ht.insert_point(HealthPoints.Heart.copy())
        ht.insert_point(HealthPoints.Splanch.copy())
        ht.insert_point(HealthPoints.Phylactery.copy())
        ht.insert_point(HealthPoints.Arm.copy())
        ht.insert_point(HealthPoints.Arm.copy())
        # init log
        log = []
        log.append("{0}, {1}".format(repr(ht), "Dead" if ht.is_dead() else "Not dead"))
        self.update_log(log)
        # draw first frame
        blt.open()
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
                    if not ht.is_dead():
                        ht.inflict_damage()
                        log.append("{0}, {1}".format(repr(ht), "Dead" if ht.is_dead() else "Not dead"))
                        self.update_log(log)
                    self.root.draw(ivec(0,0))
                    blt.refresh()
        blt.close()

i = Interface()
i.run()
