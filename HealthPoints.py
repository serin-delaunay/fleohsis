
# coding: utf-8
from HealthPoint import HealthPoint

def get_health_point(health_point : str) -> HealthPoint:
    return globals()[health_point].copy()

Heart = HealthPoint("Heart",
                    ['Body Type'],
                    [],
                    ['Dead'])

Splanch = HealthPoint("Splanch",
                      ['Body Type'],
                      ['Alive'],
                      [])

Kidney = HealthPoint("Kidney",
                     ['Body Type'],
                     ['Alive'],
                     [])

Arm = HealthPoint("Arm",
                  ['Body Type'],
                  ['Attack','Normal Attack'],
                  [])

Spear = HealthPoint("Spear",
                    ['Equipment Type','Weapon Type'],
                    ['Attack','Piercing Attack'],
                    [])

Phylactery = HealthPoint("Phylactery",
                         ['Equipment Type'],
                         ['Undead'],
                         [])


