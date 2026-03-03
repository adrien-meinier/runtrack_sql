import mysql.connector

try:
    # Connexion à la base de données
    connexion = mysql.connector.connect(
        host="localhost",        # Adresse du serveur MySQL
        user="root",             # Votre utilisateur MySQL
        password="noein210494",    # Votre mot de passe
        database="LaPlateforme"  # Nom de la base de données
    )

    print("Connexion réussie à la base de données LaPlateforme")

    # Création du curseur
    curseur = connexion.cursor()

    # Requête SQL
    requete = "SELECT * FROM etudiant"
    curseur.execute(requete)

    # Récupération des résultats
    resultats = curseur.fetchall()

    # Affichage des étudiants
    print("\nListe des étudiants :\n")
    for etudiant in resultats:
        print(etudiant)

except mysql.connector.Error as erreur:
    print("Erreur lors de la connexion à MySQL :", erreur)

finally:
    if connexion.is_connected():
        curseur.close()
        connexion.close()
        print("\nConnexion fermée.")