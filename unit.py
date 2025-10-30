from academicelement import AcademicElement

class Unit(AcademicElement):
    """Représente une unité d’enseignement composée de modules"""

    def __init__(self, code, title, coef=1):
        super().__init__(code, title, coef)
        self.modules = []

    def add_module(self, module):
        """Ajoute un module à l’unité"""
        self.modules.append(module)

    def calculate_average(self):
        """Calcule la moyenne pondérée de l’unité"""
        if not self.modules:
            return 0
        total, total_coef = 0, 0
        for m in self.modules:
            total += m.calculate_average() * m.coef
            total_coef += m.coef
        return total / total_coef if total_coef != 0 else 0

    def calculate_credits(self):
        """Retourne la somme des crédits validés des modules"""
        total_credits = 0
        for m in self.modules:
            total_credits += m.calculate_credits()
        return total_credits
