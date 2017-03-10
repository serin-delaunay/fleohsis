
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

Ability("Resist Damage (Point)", "",
        resist_damage_point='resist_damage')

Ability("Resist Damage (Tableau)", "",
        resist_damage_tableau='resist_damage')

Ability("Body Type", "Represents a part or quality of the body")

Ability("Mental Type", "Represents a part or quality of the mind")

Ability("Magic Type", "Represents a supernatural effect or capability")

Ability("Equipment Type", "Represents a piece of equipment")

Ability("Armour Type", "Represents a piece of armour")

Ability("Weapon Type", "Represents a weapon")

Ability("Shield Type", "Represents a shield")
