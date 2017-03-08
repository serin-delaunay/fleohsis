
# coding: utf-8
from Ability import Ability

def get_ability(ability : str) -> Ability:
    return globals()[ability]

Alive = Ability("Alive", "Able to sustain life")

Dead = Ability("Dead", "Too injured to sustain life")

Undead = Ability("Undead", "Animated by necromancy")

Attack = Ability("Attack", "Can attack enemies",
                 target='target_normal')
