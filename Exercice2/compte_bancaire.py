
class CompteBancaire:

    def __init__(self, solde_depart=0.0):
        # Enregistrer le solde initial dans un attribut privé
        self.__solde = solde_depart

    def deposer(self, montant):
        # Ajouter de l'argent uniquement si le montant est positif
        if montant > 0:
            self.__solde += montant
            print(f"Dépôt de {montant} € effectué.")
        else:
            print("Le montant du dépôt est invalide.")

    def retirer(self, montant):
        # Vérifier que le retrait est possible
        if 0 < montant <= self.__solde:
            self.__solde -= montant
            print(f"Retrait de {montant} € effectué.")
        else:
            print("Retrait impossible : montant invalide ou solde insuffisant.")

    def get_solde(self):
        # Retourner le solde sans autoriser sa modification directe
        return self.__solde
