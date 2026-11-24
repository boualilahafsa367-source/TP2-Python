# Exercice 1 : Compte bancaire

**Figure 1 : Exécution du programme – Gestion et protection d'un compte bancaire**

<img width="1920" height="413" alt="image" src="https://github.com/user-attachments/assets/f2cbb417-8014-4c6c-8b0f-bd32288b2d14" />


Cet exercice consiste à développer une classe CompteBancaire permettant de représenter un compte bancaire et de gérer les opérations financières tout en appliquant les principes de l'encapsulation en Python.

L'objectif principal est de protéger les données internes de l'objet et de contrôler la manière dont elles peuvent être consultées ou modifiées. Pour cela, deux attributs sont utilisés : _titulaire, qui représente le nom du propriétaire du compte et suit la convention des attributs protégés, et __solde, qui représente le montant disponible sur le compte et utilise le mécanisme de nommage privé de Python (name mangling).

La classe possède un constructeur __init__() qui initialise le titulaire et le solde de départ. Une vérification est effectuée afin d'empêcher la création d'un compte avec un solde initial négatif. La méthode deposer(montant) permet d'ajouter de l'argent au compte lorsque le montant fourni est strictement positif. La méthode retirer(montant) permet de diminuer le solde uniquement lorsque le montant demandé est valide et que les fonds disponibles sont suffisants.

Une propriété solde, définie avec le décorateur @property, permet de consulter le montant disponible sans donner un accès direct à sa modification. Cette propriété joue donc le rôle d'une interface de lecture entre l'utilisateur et les données internes de la classe. En l'absence d'un setter, toute tentative d'affectation directe à compte.solde provoque une exception AttributeError. Enfin, la méthode spéciale __str__() fournit une représentation lisible des informations du compte lors de son affichage.

Pendant l'exécution, un compte bancaire est créé pour une titulaire avec un solde initial de 1850 €. Le programme effectue ensuite un dépôt de 275 €, suivi d'un retrait de 425 €. Après ces opérations, la méthode d'affichage permet de consulter les informations du compte et la propriété solde affiche le montant restant, qui est de 1700 €.

Une dernière opération consiste à essayer de modifier directement le solde depuis l'extérieur de la classe. Cette tentative est interceptée à l'aide d'un bloc try/except, et le programme affiche un message indiquant que la modification est refusée.

Le résultat obtenu dans le terminal confirme que les opérations de dépôt et de retrait fonctionnent correctement, que le solde peut être consulté à travers une propriété et que sa modification directe est empêchée. Cet exercice permet ainsi de comprendre l'importance de l'encapsulation pour protéger les données d'un objet et garantir leur cohérence.

# Exercice 2 : Association entre classes via la composition

**Figure 2 : Exécution du programme – Gestion d'un client et de son compte bancaire par composition**

<img width="1920" height="485" alt="image" src="https://github.com/user-attachments/assets/0edd3b77-abfe-4042-85d1-80ccd881b861" />


Cet exercice consiste à mettre en œuvre une association entre deux classes en utilisant le principe de la composition. L'objectif est de comprendre comment une classe peut contenir et utiliser un objet appartenant à une autre classe, sans avoir recours à l'héritage.

Le programme est organisé autour de deux classes principales : CompteBancaire et Client. La classe CompteBancaire est responsable de la gestion du solde et des opérations financières. Elle possède un attribut privé __solde, initialisé dans son constructeur, ainsi que les méthodes deposer(), retirer() et get_solde().

La méthode deposer() permet d'augmenter le solde lorsque le montant est positif. La méthode retirer() vérifie que le montant demandé est valide et que le compte dispose de fonds suffisants avant d'effectuer le retrait. La méthode get_solde() permet de récupérer la valeur du solde sans exposer directement l'attribut privé.

La deuxième classe, Client, représente une personne possédant un compte bancaire. Elle contient deux attributs : nom, qui permet d'identifier le client, et compte, qui référence un objet de la classe CompteBancaire. Dans le constructeur de Client, une nouvelle instance de CompteBancaire est créée et affectée à l'attribut self.compte. Cette instruction représente concrètement la composition : un objet client contient un objet compte bancaire.

La méthode afficher() permet de présenter les informations du client et son solde actuel. Pour obtenir ce dernier, elle fait appel à la méthode get_solde() de l'objet contenu dans self.compte. Ainsi, chaque classe conserve une responsabilité précise : la classe CompteBancaire gère les opérations financières, tandis que la classe Client organise les informations relatives au propriétaire du compte.

Pendant l'exécution, un client nommé Salma est créé avec un solde initial de 420 €. Deux opérations sont ensuite réalisées à travers son compte : un dépôt de 180 € et un retrait de 65 €. La méthode afficher() est finalement appelée afin de présenter la situation du client.

Le résultat affiché dans le terminal confirme que les deux opérations ont été exécutées correctement et que le solde final est de 535 €. Il montre également que la classe Client peut utiliser les méthodes de l'objet CompteBancaire qu'elle contient, sans accéder directement à son attribut privé.

Cet exercice permet donc de comprendre la relation de type « a un » (has-a relationship) entre deux classes. Il met en évidence l'intérêt de la composition pour organiser un programme en plusieurs composants indépendants, réutilisables et ayant chacun une responsabilité bien définie.
