import pytest
from module import module
from unit import Unit
from semester import Semester


@pytest.fixture
def semester_sample():
    """Creates a Semester with two Units and four Modules."""
    # Unit 1
    m1 = module("F111", "Réseaux", 2, 4, 20, 10, 10, "Cours+TD+TP", 40, 60)
    m1.set_grade(td=14, tp=16, exam=12)
    m2 = module("F112", "Algo", 3, 6, 20, 10, 10, "Cours+TD+TP", 40, 60)
    m2.set_grade(td=15, tp=13, exam=14)
    u1 = Unit("UEF11", "UE Fondamentales")
    u1.add_module(m1)
    u1.add_module(m2)

    # Unit 2
    m3 = module("M111", "BD", 2, 4, 20, 10, 10, "Cours+TD+TP", 40, 60)
    m3.set_grade(td=15, tp=14, exam=13)
    m4 = module("M112", "Implémentation", 3, 5, 20, 10, 10, "Cours+TD+TP", 40, 60)
    m4.set_grade(td=14, tp=15, exam=14)
    u2 = Unit("UEM11", "UE Méthodologie")
    u2.add_module(m3)
    u2.add_module(m4)

    # Semester
    s = Semester("S1")
    s.add_unit(u1)
    s.add_unit(u2)

    return s
  

def test_semester_average(semester_sample):
    assert round(semester_sample.calculate_average(), 2) == pytest.approx(14.02, rel=1e-2)


def test_semester_total_credits(semester_sample):
    assert semester_sample.calculate_credits() == 19  # 10 + 9