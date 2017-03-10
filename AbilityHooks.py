
# coding: utf-8
from typing import Dict, Any, Callable, Optional
from hook_priority import hook_priority
from Logger import messages, debug

EventArgs = Dict[str,Any]
EventHook = Callable[[EventArgs],None]

def get_hook(hook : str) -> EventHook:
    return globals()[hook]

@hook_priority(0)
def begin_attack(event_args : EventArgs):
    debug.log('beginning attack')
    event_args['targetted_health_point'] = None
    event_args['attack_abilities'].call('target_health_point', event_args)
    targetted_health_point = event_args['targetted_health_point']
    if targetted_health_point is not None:
        debug.log('targetted health point: {0}'.format(targetted_health_point))
        if targetted_health_point.is_healthy:
            debug.log('targetted health point is healthy')
            event_args['damage_resisted'] = False
            targetted_health_point.get_abilities().call('resist_damage_point', event_args)
            event_args['defender'].call('resist_damage_tableau', event_args)
            if not event_args['damage_resisted']:
                targetted_health_point.is_healthy = False
                debug.log('damage taken')
                return
        else:
            debug.log('targetted health point is already damaged')
    else:
        debug.log('failed to target health point')

@hook_priority(0)
def target_normal(event_args : EventArgs):
    debug.log('finding target health point')
    for health_point in reversed(event_args['defender']):
        if health_point.is_healthy:
            debug.log('found valid target: {0}'.format(health_point))
            event_args['targetted_health_point'] = health_point
            return
    debug.log('found no valid target')

@hook_priority(0)
def target_piercing(event_args : EventArgs):
    pass

@hook_priority(0)
def resist_damage(event_args : EventArgs):
    debug.log('resisting damage')
    event_args['damage_resisted'] = True
