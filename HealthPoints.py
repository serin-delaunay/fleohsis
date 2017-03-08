
# coding: utf-8
import HealthPoint

def get_health_point(health_point : str) -> HealthPoint:
    return globals()[health_point]

Heart = HealthPoint.HealthPoint("Heart",[],['Dead'])

Splanch = HealthPoint.HealthPoint("Splanch",['Alive'],[])

Kidney = HealthPoint.HealthPoint("Kidney",['Alive'],[])

Arm = HealthPoint.HealthPoint("Arm",['Attack'],[])

Phylactery = HealthPoint.HealthPoint("Phylactery",['Undead'],[])
