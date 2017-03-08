
# coding: utf-8
from sortedcontainers import SortedListWithKey
from collections import defaultdict, Counter
from AbilityHooks import EventHook
from typing import Dict, Any, NamedTuple

class EventHookBag(object):
    def __init__(self) -> None:
        self._hook_counter = Counter()
        self._hooks = defaultdict(lambda:SortedListWithKey(key=lambda x: x.priority))
    def add_hook(self, event : str, hook : EventHook) -> None:
        self._hook_counter[(event,hook)] += 1
        if self._hook_counter[(event,hook)] == 1:
            self._hooks[event].add(hook)
    def remove_hook(self, event : str, hook : EventHook) -> None:
        self._hook_counter[(event, hook)] -= 1
        if self._hook_counter[(event, hook)] == 0:
            self._hooks[event].remove(hook)
        self._clean_counter()
    def call(self, event : str, event_args : Dict[str, Any]):
        if event in self._hooks:
            for hook in self._hooks[event]:
                hook(event_args)
    def _clean_counter(self)->None:
        self._hook_counter = Counter({k:v for k,v in _hook_counter.items() if v != 0})
