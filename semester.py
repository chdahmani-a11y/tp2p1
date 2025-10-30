# semester.py

from unit import Unit

class Semester(Unit):
    def __init__(self, name, units=None):
        super().__init__(name, coefficient=1)
        self.units = units if units else []

    def add_unit(self, unit):
        self.units.append(unit)

    def compute_average(self):
        """Calcul de la moyenne générale du semestre."""
        total_weight = sum(u.coefficient for u in self.units)
        total_score = sum(u.compute_average() * u.coefficient for u in self.units)
        return round(total_score / total_weight, 2) if total_weight else 0

    def total_credits(self):
        """Total des crédits validés dans le semestre."""  
        return sum(u.credits for u in self.units) 

