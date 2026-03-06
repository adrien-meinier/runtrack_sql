import mysql.connector

try:
    # Connexion à la base de données
    connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="LaPlateforme"
    )

    curseur = connexion.cursor()

    # Requête SQL
    requete = "SELECT nom, capacite FROM salle"
    curseur.execute(requete)

    # Récupération des résultats
    resultats = curseur.fetchall()

    # Affichage en console
    print("Liste des salles et leur capacité :\n")
    for nom, capacite in resultats:
        print(f"Salle : {nom} | Capacité : {capacite}")

except mysql.connector.Error as erreur:
    print("Erreur :", erreur)

finally:
    if connexion.is_connected():
        curseur.close()
        connexion.close()
        print("\nConnexion fermée.")