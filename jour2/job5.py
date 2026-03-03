import mysql.connector

try:
    connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="noein210494",
        database="LaPlateforme"
    )

    curseur = connexion.cursor()

    requete = "SELECT SUM(superficie) FROM etage"
    curseur.execute(requete)

    resultat = curseur.fetchone()
    superficie_totale = resultat[0]

    print(f"La superficie de La Plateforme est de {superficie_totale} m2")

except mysql.connector.Error as erreur:
    print("Erreur :", erreur)

finally:
    if connexion.is_connected():
        curseur.close()
        connexion.close()