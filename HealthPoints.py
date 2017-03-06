
# coding: utf-8
import HealthPoint
import Ability
import Abilities

Heart = HealthPoint.HealthPoint("Heart",[],[Abilities.Dead])

Splanch = HealthPoint.HealthPoint("Splanch",[Abilities.Alive],[])

Kidney = HealthPoint.HealthPoint("Kidney",[Abilities.Alive],[])

Arm = HealthPoint.HealthPoint("Arm",[Abilities.Attack],[])

Phylactery = HealthPoint.HealthPoint("Phylactery",[Abilities.Undead],[])
