class AcademicElement:
    """Classe de base pour les éléments académiques (Module, Unité, Semestre)"""

    def __init__(self, code, title, coef=1):
        self.code = code
        self.title = title
        self.coef = coef

    def calculate_average(self):
        """Méthode à redéfinir dans les classes filles"""
        pass

    def calculate_credits(self):
        """Méthode à redéfinir dans les classes filles"""
        pass
