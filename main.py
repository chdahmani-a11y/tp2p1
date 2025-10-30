from module import Module
from unit import Unit
from semester import Semester

if __name__ == "__main__":
    # Création des modules
    m1 = Module("ALG", "Algorithmique", coef=2, credit=4)
    m1.set_grade(tp=14, td=15, exam=16)

    m2 = Module("POO", "Programmation OO", coef=3, credit=5)
    m2.set_grade(tp=12, td=13, exam=14)

    m3 = Module("BD", "Bases de Données", coef=2, credit=4)
    m3.set_grade(tp=15, td=14, exam=15)

    # Création des unités
    u1 = Unit("UEF11", "UE Fondamentale", coef=2)
    u1.add_module(m1)
    u1.add_module(m2)

    u2 = Unit("UEF12", "UE Spécialisée", coef=3)
    u2.add_module(m3)

    # Création du semestre
    sem = Semester("S1", "Semestre 1")
    sem.add_unit(u1)
    sem.add_unit(u2)

    print("=== Résultats ===")
    print(f"Moyenne module ALG : {m1.calculate_average():.2f}")
    print(f"Moyenne unité UEF11 : {u1.calculate_average():.2f}")
    print(f"Moyenne semestre S1 : {sem.calculate_average():.2f}")
    print(f"Crédits semestre S1 : {sem.calculate_credits()}")
