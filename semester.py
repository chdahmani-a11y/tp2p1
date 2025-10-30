from academicelement import AcademicElement

class Semester(AcademicElement):
    """Représente un semestre contenant plusieurs unités d’enseignement"""

    def __init__(self, code, title):
        super().__init__(code, title)
        self.units = []

    def add_unit(self, unit):
        """Ajoute une unité au semestre"""
        self.units.append(unit)

    def calculate_average(self):
        """Calcule la moyenne pondérée du semestre"""
        if not self.units:
            return 0
        total, total_coef = 0, 0
        for u in self.units:
            total += u.calculate_average() * u.coef
            total_coef += u.coef
        return total / total_coef if total_coef != 0 else 0

    def calculate_credits(self):
        """Retourne la somme des crédits validés des unités"""
        total_credits = 0
        for u in self.units:
            total_credits += u.calculate_credits()
        return total_credits
