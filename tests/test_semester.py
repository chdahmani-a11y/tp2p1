import pytest
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from unit import Unit
from module import Module
from semester import Semester

def test_semester_average_and_credits():
    m1 = Module("ALG", "Algorithmique", coef=2, credit=4)
    m1.set_grade(tp=14, td=15, exam=16)

    m2 = Module("POO", "Programmation OO", coef=3, credit=5)
    m2.set_grade(tp=12, td=13, exam=14)

    m3 = Module("BD", "Bases de Données", coef=2, credit=4)
    m3.set_grade(tp=15, td=14, exam=15)

    u1 = Unit("UEF11", "UE Fondamentale", coef=2)
    u1.add_module(m1)
    u1.add_module(m2)

    u2 = Unit("UEF12", "UE Spécialisée", coef=3)
    u2.add_module(m3)

    sem = Semester("S1", "Semestre 1")
    sem.add_unit(u1)
    sem.add_unit(u2)

    assert round(sem.calculate_average(), 2) == 14.56
    assert sem.calculate_credits() == 13
