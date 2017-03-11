
# coding: utf-8
from Logger import debug
from typing import Optional, Any, Callable, Dict

EventArgs = Dict[str,Any]
EventHook = Callable[[EventArgs],None]

ERROR_ON_UNREGISTERED_EVENT = False

def check_event(event: str) -> None:
    if ERROR_ON_UNREGISTERED_EVENT:
        assert event in _events, event
    else:
        if event not in _events: debug.log('event {0} not registered'.format(event))

def register_event(event: str) -> None:
    assert(event not in _events)
    _events.add(event)

_events = {
    'list_attack_modes',
    'prepare_attack',
    'base_attack',
    'augment_attack',
    'execute_attack',
    'target_health_point',
}
