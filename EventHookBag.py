
# coding: utf-8
from sortedcontainers import SortedListWithKey
from collections import defaultdict, Counter
from Events import EventHook
from typing import Dict, Any, NamedTuple
from Logger import debug
from Events import check_event

class EventHookBag(object):
    def __init__(self) -> None:
        self._hook_counter = Counter()
        self._hooks = defaultdict(lambda:SortedListWithKey(key=lambda x: x.priority))
    def add_hook(self, event : str, hook : EventHook) -> None:
        check_event(event)
        debug.log('adding hook for event {0}'.format(event))
        self._hook_counter[(event,hook)] += 1
        if self._hook_counter[(event,hook)] == 1:
            debug.log('hook is new for event, adding to call list')
            self._hooks[event].add(hook)
    def remove_hook(self, event : str, hook : EventHook) -> None:
        self._hook_counter[(event, hook)] -= 1
        if self._hook_counter[(event, hook)] == 0:
            self._hooks[event].remove(hook)
        self._clean_counter()
    def call(self, event : str, event_args : Dict[str, Any]):
        check_event(event)
        debug.log('event called : {0}'.format(event))
        if event in self._hooks:
            debug.log('{0} hooks handling it'.format(len(self._hooks[event])))
            for hook in self._hooks[event]:
                hook(event_args)
        else:
            debug.log('no hooks for this event')
    def _clean_counter(self)->None:
        self._hook_counter = Counter({k:v for k,v in self._hook_counter.items() if v != 0})
