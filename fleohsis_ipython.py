
# coding: utf-8

# In[ ]:

from bearlibterminal import terminal as blt


# In[ ]:

get_ipython().magic('load_ext autoreload')


# In[ ]:

get_ipython().magic('aimport Ability')
get_ipython().magic('aimport Abilities')
get_ipython().magic('aimport HealthPoint')
get_ipython().magic('aimport HealthPoints')
get_ipython().magic('aimport HealthTableau')
get_ipython().magic('aimport FPSLimiter')


# In[ ]:

get_ipython().magic('autoreload')


# In[ ]:

def main() -> None:
    blt.open()
    log = []
    ht = HealthTableau.HealthTableau()
    ht.insert_point(HealthPoints.Heart.copy())
    ht.insert_point(HealthPoints.Splanch.copy())
    ht.insert_point(HealthPoints.Phylactery.copy())
    ht.insert_point(HealthPoints.Arm.copy())
    ht.insert_point(HealthPoints.Arm.copy())
    while not ht.is_dead():
        log.append("{0}, {1}".format(repr(ht), "Dead" if ht.is_dead() else "Not dead"))
        ht.inflict_damage()
    log.append("{0}, {1}".format(repr(ht), "Dead" if ht.is_dead() else "Not dead"))
    for x in log:
        print(x)
    blt.printf(0,0,'[bbox=80x20]'+'\n'.join(log))
    fps_limiter = FPSLimiter.FPSLimiter()
    blt.set('window:title="FLEOHSIS ({0} FPS)"'.format(fps_limiter.get_fps()))
    blt.refresh()
    while blt.read() != blt.TK_CLOSE:
        fps_limiter.wait()
        blt.set('window:title="FLEOHSIS ({0} FPS)"'.format(fps_limiter.get_fps()))
    blt.close()


# In[ ]:

if __name__ == '__main__':
    main()

