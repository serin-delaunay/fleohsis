
# coding: utf-8
from Ability import Ability, _abilities

def get_ability(ability : str) -> Ability:
    return _abilities[ability]

Ability("Alive", "Able to sustain life")

Ability("Dead", "Too injured to sustain life")

Ability("Undead", "Animated by necromancy")

Ability("Target Attack (Piercing)", "", True,
        target_health_point='target_piercing')

Ability("Target Attack (Normal)", "", True,
        target_health_point='target_normal')

Ability("Attack", "", True,
        list_attack_modes='register_weapon',
        prepare_attack='prepare_attack',
        execute_attack='execute_attack',)

Ability("Normal Attack", "Performs a normal attack",
        base_attack=[
            'base_attack_abilities_default',
            'base_attack_points_default'])

Ability("Piercing Attack", "Performs a piercing attack",
        base_attack=[
            'base_attack_abilities_default',
            'base_attack_points_piercing'])

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
