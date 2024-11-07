class TestRunner:
    """Classe pour exécuter des tests et afficher les résultats."""

    # Codes ANSI pour les couleurs
    GREEN = '\033[92m'  # Vert
    RED = '\033[91m'    # Rouge
    YELLOW = '\033[93m'  # Jaune
    RESET = '\033[0m'   # Reset

    def __init__(self, test_classes):
        self.test_classes = test_classes
        self.total_tests = 0  
        self.total_success = 0  
        self.total_failures = 0  

    def run(self, debug=False):
        """Exécute les tests dans les classes spécifiées.

        Args:
            debug (bool): Si True, affiche les résultats détaillés des tests.
        """
        for test_class in self.test_classes:
            print(f"\n=== Classe de Test : {test_class.__name__} ===")  # Titre de la classe de test
            test_instance = test_class()  # Crée une instance de la classe de test
            class_success = 0  # Nombre de tests réussis dans la classe
            class_failures = 0  # Nombre de tests échoués dans la classe
            class_total = 0  # Nombre total de tests dans la classe

            for method_name in dir(test_instance):
                if method_name.startswith("test_"):  # Filtre pour les méthodes de test
                    method = getattr(test_instance, method_name)
                    if callable(method):
                        class_total += 1  # Incrémente le total des tests à chaque itération
                        try:
                            # Exécution du test
                            result = method()  # On s'attend à ce que la méthode de test retourne True ou False
                            if result:
                                class_success += 1
                                self.total_success += 1
                                output = f"{self.GREEN}Réussite : {method_name}{self.RESET}"
                            else:
                                class_failures += 1
                                self.total_failures += 1
                                output = f"{self.RED}Échec : {method_name}{self.RESET}"
                        except Exception as e:
                            # En cas d'exception, on l'affiche et on la compte comme un échec
                            class_failures += 1
                            self.total_failures += 1
                            output = f"{self.RED}Erreur : {self.YELLOW}{str(e)}{self.RESET} dans {method_name}"
                        
                        print(f"    {output}")  # Affichage avec indentation

                        if debug:
                            print(f"        Détails : {output}")

            # Résumé de la classe
            print(f"\nRésumé de {test_class.__name__}:")
            print(f"    Total tests: {class_total}")
            print(f"    Tests réussis: {class_success}")
            print(f"    Tests échoués: {class_failures}")

            # Mise à jour du total des tests dans la classe
            self.total_tests += class_total

        # Résumé global
        print(f"\n=== Résumé Global ===")
        print(f"    Total tests: {self.total_tests}")
        print(f"    Tests réussis: {self.total_success}")
        print(f"    Tests échoués: {self.total_failures}")
        if self.total_failures == 0:
            print(f"{self.GREEN}Tous les tests ont réussi !{self.RESET}")
        else:
            print(f"{self.RED}Certains tests ont échoué.{self.RESET}")


# Exemple de classe de test
class ExampleTests:
    """Exemple de classe de tests pour démonstration."""

    def test_success(self):
        """Test qui réussit."""
        return True

    def test_failure(self):
        """Test qui échoue."""
        return False

    def test_exception(self):
        """Test qui génère une exception."""
        raise ValueError("Erreur dans le test")
# Exemple de classe de test
class ExampleTestsBis:
    """Exemple de classe de tests pour démonstration."""

    def test_success(self):
        """Test qui réussit."""
        return True

    def test_failure(self):
        """Test qui échoue."""
        return False

    def test_exception(self):
        """Test qui génère une exception."""
        raise ValueError("Erreur dans le test")


# Utilisation de TestRunner
if __name__ == "__main__":
    runner = TestRunner([ExampleTests,ExampleTestsBis])  # Crée une instance de TestRunner avec la classe de test
    runner.run(debug=True)  # Exécute les tests avec le mode débogage activé
