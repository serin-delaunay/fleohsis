
# coding: utf-8
import HealthPoint

def get_health_point(health_point : str) -> HealthPoint:
    return globals()[health_point].copy()

Heart = HealthPoint.HealthPoint("Heart",
                                ['Body Type'],
                                [],
                                ['Dead'])

Splanch = HealthPoint.HealthPoint("Splanch",
                                  ['Body Type'],
                                  ['Alive'],
                                  [])

Kidney = HealthPoint.HealthPoint("Kidney",
                                 ['Body Type'],
                                 ['Alive'],
                                 [])

Arm = HealthPoint.HealthPoint("Arm",
                              ['Body Type'],
                              ['Attack'],
                              [])

Phylactery = HealthPoint.HealthPoint("Phylactery",
                                     ['Equipment Type'],
                                     ['Undead'],
                                     [])
