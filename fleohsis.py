# coding: utf-8

from bearlibterminal import terminal as blt

import Ability
import Abilities
import HealthPoint
import HealthPoints
import HealthTableau
import FPSLimiter

def main() -> None:
    # init health
    ht = HealthTableau.HealthTableau()
    ht.insert_point(HealthPoints.Heart.copy())
    ht.insert_point(HealthPoints.Splanch.copy())
    ht.insert_point(HealthPoints.Phylactery.copy())
    ht.insert_point(HealthPoints.Arm.copy())
    ht.insert_point(HealthPoints.Arm.copy())
    # init log
    log = []
    log.append("{0}, {1}".format(repr(ht), "Dead" if ht.is_dead() else "Not dead"))
    # draw first frame
    blt.open()
    blt.printf(0,0,'[bbox=80x20]'+'\n'.join(log))
    fps_limiter = FPSLimiter.FPSLimiter()
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
                blt.printf(0,0,'[bbox=80x20]'+'\n'.join(log))
                blt.refresh()
    blt.close()

if __name__ == '__main__':
    main()
