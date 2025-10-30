import pytest
from module import Module


@pytest.fixture
def module_sample():
    """Fixture: Creates a sample Module object."""
    m = module(
        "F111", "Réseaux des couches basses",
        coef=3, credit=6,
        vh_cours=22.5, vh_td=22.5, vh_tp=22.5,
        mode="Cours+TD+TP",
        pourc_continu=40, pourc_exam=60
    )
    return m


def test_module_average_with_td_tp_exam(module_sample):
    module_sample.set_grade(td=14, tp=16, exam=12)
    assert round(module_sample.calculate_average(), 2) == pytest.approx(13.6, rel=1e-2)


def test_module_credit_valid(module_sample):
    module_sample.set_grade(td=15, tp=14, exam=13)
    assert module_sample.calculate_credits() == 6


def test_module_credit_fail(module_sample):
    module_sample.set_grade(td=5, tp=6, exam=8)
    assert module_sample.calculate_credits() == 0


def test_invalid_grade_raises(module_sample):
    with pytest.raises(ValueError):
        module_sample.set_grade(td=25)  # invalid