
# coding: utf-8
from typing import Dict, Any, Callable
from hook_priority import hook_priority

EventArgs = Dict[str,Any]
EventHook = Callable[[EventArgs],None]

def get_ability(hook : str) -> EventHook:
    return globals()[hook]

@hook_priority(1)
def target_normal(event_args : EventArgs):
    if 'target_found' in event_args:
        return
