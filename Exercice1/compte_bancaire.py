
class CompteBancaire:

    def __init__(self, titulaire, solde_initial=0):
        # Enregistrer le nom du titulaire
        self._titulaire = titulaire

        # Vérifier que le solde initial n'est pas négatif
        if solde_initial < 0:
            raise ValueError("Le solde initial ne peut pas être négatif.")

        # Initialiser le solde comme attribut privé
        self.__solde = solde_initial

    def deposer(self, montant):
        # Vérifier que le montant à déposer est positif
        if montant > 0:
            self.__solde += montant
            print(f"Dépôt effectué : {montant} €")
        else:
            print("Montant invalide pour le dépôt.")

    def retirer(self, montant):
        # Vérifier le montant et la disponibilité des fonds
        if 0 < montant <= self.__solde:
            self.__solde -= montant
            print(f"Retrait effectué : {montant} €")
        else:
            print("Fonds insuffisants ou montant invalide.")

    @property
    def solde(self):
        # Autoriser uniquement la lecture du solde
        return self.__solde

    def __str__(self):
        # Fournir une présentation claire du compte
        return f"Titulaire : {self._titulaire}, Solde : {self.solde} €"
