
from compte_bancaire import CompteBancaire


class Client:

    def __init__(self, nom, solde_depart=0.0):
        # Enregistrer le nom du client
        self.nom = nom

        # Créer un compte bancaire appartenant au client
        self.compte = CompteBancaire(solde_depart)

    def afficher(self):
        # Récupérer le solde depuis l'objet CompteBancaire
        montant = self.compte.get_solde()

        # Afficher les informations du client
        print(f"Client : {self.nom}, Solde : {montant} €")
