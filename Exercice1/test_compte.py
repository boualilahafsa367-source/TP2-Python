
from compte_bancaire import CompteBancaire


if __name__ == "__main__":

    # Créer un nouveau compte bancaire
    compte = CompteBancaire("Meriem", 1850)

    # Effectuer quelques opérations
    compte.deposer(275)
    compte.retirer(425)

    # Afficher les informations du compte
    print("\nInformations du compte :")
    print(compte)

    # Consulter le solde à travers la propriété
    print("Solde actuel :", compte.solde, "€")

    # Essayer de modifier directement le solde
    try:
        compte.solde = 500
    except AttributeError as erreur:
        print("Modification refusée :", erreur)
