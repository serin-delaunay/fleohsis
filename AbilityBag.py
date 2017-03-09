
# coding: utf-8
from collections import Counter
from typing import List, Union, Optional, Iterator
from Ability import Ability
from Abilities import get_ability
from EventHookBag import EventHookBag
from sortedcontainers import SortedListWithKey
from Logger import debug

class AbilityBag(object):    
    def __init__(self, abilities: List[str] = []) -> None:
        self._ability_counter = Counter()
        self._hooks = EventHookBag()
        self.add_abilities(abilities)
    def add_abilities(self, abilities: List[Union[str,Ability]] = []) -> None:
        abilities = [x if isinstance(x,str) else x.name for x in abilities]
        debug.log('adding abilities {0} to bag'.format(abilities))
        self._ability_counter.update(abilities)
        for ability in abilities:
            debug.log('adding ability {0} to bag'.format(ability))
            ability = get_ability(ability)
            if self._ability_counter[ability.name] == 1:
                debug.log('ability is new, updating event hooks')
                for event, hook in ability.hooks.items():
                    self._hooks.add_hook(event, hook)
            else:
                debug.log('ability is not new (count={0})'.format(
                    self._ability_counter[ability.name]))
    def remove_abilities(self, abilities: List[Union[str,Ability]]) -> None:
        abilities = [x if isinstance(x,str) else x.name for x in abilities]
        self._ability_counter.subtract(abilities)
        for ability in abilities:
            if isinstance(ability,str):
                ability = get_ability(ability)
            if self._ability_counter[ability.name] == 0:
                for event, hook in ability.hooks.items():
                    self._hooks.remove_hook(event, hook)
        self._clean_counter()
    def has_ability(self, ability: Union[str, Ability]) -> bool:
        if isinstance(ability, Ability):
            return self._ability_counter[ability.name] > 0
        else:
            return self._ability_counter[ability] > 0
    def call(self, event, event_args):
        self._hooks.call(event, event_args)
    def _clean_counter(self):
        self._ability_counter = Counter(
            {k:v for k,v in self._ability_counter.items() if v != 0})
    def names(self) -> Iterator[str]:
        return iter(self._ability_counter)
    def abilities(self) -> Iterator[Ability]:
        return map(get_ability, self.names())
