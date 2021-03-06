
# coding: utf-8
from typing import Optional, List
from hook_priority import hook_priority
from Logger import messages, debug
from Events import EventArgs, EventHook

def get_hook(hook : str) -> EventHook:
    return globals()[hook]

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
    debug.log('finding target health point')
    found_healthy_point = False
    for health_point in reversed(event_args['defender']):
        if health_point.is_healthy:
            if not found_healthy_point:
                found_healthy_point = True
                target_point = health_point
                debug.log('found first healthy point: {0}'.format(target_point))
                event_args['targetted_health_point'] = target_point
                event_args['point_to_bypass'] = target_point
                event_args['bypass_successful'] = True
                target_point.get_abilities().call('resist_bypass', event_args)
                if not event_args['bypass_successful']:
                    debug.log('bypass unsuccessful')
                    return
                else:
                    debug.log('bypass successful')
            else:
                event_args['targetted_health_point'] = health_point
                return

@hook_priority(0)
def resist_damage(event_args : EventArgs):
    debug.log('resisting damage')
    event_args['damage_resisted'] = True

def _register_weapon(attack_mode : Optional[str]=None):
    @hook_priority(0)
    def register_weapon(event_args : EventArgs):
        weapon = event_args['weapon']
        event_args['attack_modes'].append((weapon,attack_mode))
    return register_weapon

register_weapon = _register_weapon()

def _base_attack_abilities(abilities : List[str]):
    @hook_priority(0)
    def base_attack_abilities(event_args : EventArgs):
        event_args['damage_tableau'].add_common_abilities(abilities)
    return base_attack_abilities

base_attack_abilities_default = _base_attack_abilities(["Attack"])

def _add_attack_point(point : List[str]):
    @hook_priority(0)
    def base_attack_points(event_args : EventArgs):
        from DamagePoint import DamagePoint
        event_args['damage_tableau'].add_damage_point(DamagePoint(point, event_args['weapon']))
    return base_attack_points

add_attack_point_normal = _add_attack_point(["Target Attack (Normal)"])

add_attack_point_piercing = _add_attack_point(["Target Attack (Piercing)"])

@hook_priority(0)
def add_attack_point_copy(event_args : EventArgs):
    damage_tableau = event_args['damage_tableau']
    try:
        last_point = damage_tableau._damage_points[-1]
    except IndexError:
        return
    damage_tableau.add_damage_point(last_point.copy())

@hook_priority(0)
def prepare_attack(event_args : EventArgs):
    from DamageTableau import DamageTableau
    damage_tableau = DamageTableau([],[])
    event_args['damage_tableau'] = damage_tableau
    weapon = event_args['weapon']
    weapon.get_abilities().call('base_attack',event_args)

@hook_priority(0)
def execute_attack(event_args : EventArgs):
    if 'targetted_health_point' not in event_args:
        event_args['targetted_health_point'] = None
    damage_point = event_args['damage_point']
    damage_point.call('target_health_point', event_args)
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
