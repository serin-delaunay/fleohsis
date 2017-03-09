
# coding: utf-8
import HealthPoint

def get_health_point(health_point : str) -> HealthPoint:
    return globals()[health_point].copy()

Heart = HealthPoint.HealthPoint("Heart",['Take Damage'],['Dead'])

Splanch = HealthPoint.HealthPoint("Splanch",['Take Damage','Alive'],[])

Kidney = HealthPoint.HealthPoint("Kidney",['Take Damage','Alive'],[])

Arm = HealthPoint.HealthPoint("Arm",['Take Damage','Begin Attack','Target Attack (Normal)'],[])

Phylactery = HealthPoint.HealthPoint("Phylactery",['Take Damage','Undead'],[])
