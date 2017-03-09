
# coding: utf-8
from Ability import Ability, _abilities

def get_ability(ability : str) -> Ability:
    return _abilities[ability]

Ability("Alive", "Able to sustain life")

Ability("Dead", "Too injured to sustain life")

Ability("Undead", "Animated by necromancy")

Ability("Target Attack (Normal)", "", True,
        target_health_point='target_normal')

Ability("Begin Attack", "", True,
        begin_attack='begin_attack')

Ability("Take Damage", "", True,
        damage_point='take_damage')
