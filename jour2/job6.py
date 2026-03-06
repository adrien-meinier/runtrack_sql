import mysql.connector

try:
    connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="LaPlateforme"
    )

    curseur = connexion.cursor()

    requete = "SELECT SUM(capacite) FROM salle"
    curseur.execute(requete)

    resultat = curseur.fetchone()
    capacite_totale = resultat[0]

    print(f"La capacité totale des salles est de {capacite_totale} personnes")

except mysql.connector.Error as erreur:
    print("Erreur :", erreur)

finally:
    if connexion.is_connected():
        curseur.close()
        connexion.close()