import pytest
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from unit import Unit
from module import Module

def test_unit_average_and_credits():
    m1 = Module("ALG", "Algorithmique", coef=2, credit=4)
    m1.set_grade(tp=14, td=15, exam=16)

    m2 = Module("POO", "Programmation OO", coef=3, credit=5)
    m2.set_grade(tp=12, td=13, exam=14)

    u = Unit("UEF11", "UE Fondamentale", coef=2)
    u.add_module(m1)
    u.add_module(m2)

    assert round(u.calculate_average(), 2) == 14.3
    assert u.calculate_credits() == 9
