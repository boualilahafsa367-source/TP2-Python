
from client import Client


if __name__ == "__main__":

    # Créer un client avec son compte bancaire
    cliente = Client("Salma", 420)

    # Accéder au compte du client pour effectuer les opérations
    cliente.compte.deposer(180)
    cliente.compte.retirer(65)

    # Afficher le nom du client et son solde actuel
    print("\nSituation du client :")
    cliente.afficher()
