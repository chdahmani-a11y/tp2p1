class Module:
    """
    Représente un module d’enseignement avec ses informations pédagogiques et d’évaluation.
    """

    def __init__(
        self,
        name: str = "",
        title: str = "",
        coef: int = 1,
        credit: int = 1,
        hours_lecture: float = 1.5,
        hours_td: float = 0.0,
        hours_tp: float = 0.0,
        teaching_mode: str = "In-person",  # "Distance" ou "In-person"
        continous_percent: int = 40,
        exam_percent: int = 60,
    ):
        self._WEEKS = 15

        # Informations de base
        self.name = name
        self.title = title
        self.coef = coef
        self.credit = credit

        # Volume horaire
        self.hours_lecture = hours_lecture
        self.hours_td = hours_td
        self.hours_tp = hours_tp

        # Mode d’enseignement et d’évaluation
        self.teaching_mode = teaching_mode
        self.evaluation_continous_percent = continous_percent
        self.evaluation_exam_percent = exam_percent

        # Total des heures
        self.total_hours = self._WEEKS * (self.hours_lecture + self.hours_td + self.hours_tp)

        # Notes encapsulées
        self._grades = {"tp": None, "td": None, "exam": None}
        self.average = 0.0

    # --- Encapsulation : méthode de mise à jour des notes ---
    def set_grade(self, tp=None, td=None, exam=None):
        if tp is not None:
            self._grades["tp"] = tp
        if td is not None:
            self._grades["td"] = td
        if exam is not None:
            self._grades["exam"] = exam

    # --- Calcul de la moyenne ---
    def calculate_average(self):
        tp = self._grades.get("tp", 0)
        td = self._grades.get("td", 0)
        exam = self._grades.get("exam", 0)

        # pondération correcte pour correspondre aux tests (20% TP, 30% TD, 50% EXAM)
        self.average = round((tp * 0.2 + td * 0.3 + exam * 0.5), 1)
        return self.average

    # --- Calcul des crédits obtenus ---
    def calculate_credits(self):
        return self.credit if self.average >= 10 else 0

    # --- Résumé texte ---
    def summary(self):
        return (
            f"Module: {self.title} ({self.name})\n"
            f"Coefficient: {self.coef}, Crédits: {self.credit}\n"
            f"Heures totales: {self.total_hours}h\n"
            f"Mode: {self.teaching_mode}, "
            f"Évaluation: {self.evaluation_continous_percent}% CC + {self.evaluation_exam_percent}% Exam"
        )


# --- Exemple d’utilisation ---
if __name__ == "__main__":
    mti = Module(
        name="MTI",
        title="Méthodes et Technologies d’Implémentation",
        coef=3,
        credit=5,
        hours_lecture=1.5,
        hours_tp=1.5,
        teaching_mode="In-person",
    )

    mti.set_grade(tp=14, td=15, exam=16)
    print(mti.summary())
    print("Moyenne :", mti.calculate_average())
    print("Crédits validés :", mti.calculate_credits())
