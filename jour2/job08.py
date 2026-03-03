import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="noein210494",
    database="zoo"
)

cursor = conn.cursor()


def ajouter_cage():
    superficie = float(input("Superficie : "))
    capacite = int(input("Capacité maximale : "))

    sql = "INSERT INTO cage (superficie, capacite_max) VALUES (%s, %s)"
    cursor.execute(sql, (superficie, capacite))
    conn.commit()
    print("Cage ajoutée avec succès.")

def ajouter_animal():
    nom = input("Nom : ")
    race = input("Race : ")
    id_cage = int(input("ID Cage : "))
    date_naissance = input("Date de naissance (YYYY-MM-DD) : ")
    pays = input("Pays d'origine : ")

    # check capacity
    cursor.execute("SELECT COUNT(*) FROM animal WHERE id_cage = %s", (id_cage,))
    nb_animaux = cursor.fetchone()[0]

    cursor.execute("SELECT capacite_max FROM cage WHERE id_cage = %s", (id_cage,))
    result = cursor.fetchone()

    if result:
        capacite = result[0]
        if nb_animaux < capacite:
            sql = """INSERT INTO animal 
                     (nom, race, id_cage, date_naissance, pays_origine)
                     VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(sql, (nom, race, id_cage, date_naissance, pays))
            conn.commit()
            print("Animal ajouté avec succès.")
        else:
            print(" Cage pleine.")
    else:
        print("Cage inexistante.")

def supprimer_animal():
    id_animal = int(input("ID animal à supprimer : "))
    cursor.execute("DELETE FROM animal WHERE id_animal = %s", (id_animal,))
    conn.commit()
    print("Animal supprimé.")

def supprimer_cage():
    id_cage = int(input("ID cage à supprimer : "))
    cursor.execute("DELETE FROM cage WHERE id_cage = %s", (id_cage,))
    conn.commit()
    print("Cage supprimée.")

def modifier_animal():
    id_animal = int(input("ID animal à modifier : "))
    nouveau_nom = input("Nouveau nom : ")

    cursor.execute("UPDATE animal SET nom = %s WHERE id_animal = %s",
                   (nouveau_nom, id_animal))
    conn.commit()
    print("Animal modifié.")

def afficher_animaux():
    cursor.execute("SELECT * FROM animal")
    animaux = cursor.fetchall()

    print("\n--- Liste des animaux ---")
    for animal in animaux:
        print(animal)

def afficher_animaux_par_cage():
    cursor.execute("""
        SELECT cage.id_cage, animal.nom, animal.race
        FROM cage
        LEFT JOIN animal ON cage.id_cage = animal.id_cage
        ORDER BY cage.id_cage
    """)

    print("\n--- Animaux par cage ---")
    for ligne in cursor.fetchall():
        print(ligne)

def superficie_totale():
    cursor.execute("SELECT SUM(superficie) FROM cage")
    total = cursor.fetchone()[0]
    print(f"Superficie totale des cages : {total} m²")

#MENU 

while True:
    print("""
1. Ajouter une cage
2. Ajouter un animal
3. Supprimer un animal
4. Supprimer une cage
5. Modifier un animal
6. Afficher tous les animaux
7. Afficher animaux par cage
8. Superficie totale des cages
9. Quitter
""")

    choix = input("Choix : ")

    if choix == "1":
        ajouter_cage()
    elif choix == "2":
        ajouter_animal()
    elif choix == "3":
        supprimer_animal()
    elif choix == "4":
        supprimer_cage()
    elif choix == "5":
        modifier_animal()
    elif choix == "6":
        afficher_animaux()
    elif choix == "7":
        afficher_animaux_par_cage()
    elif choix == "8":
        superficie_totale()
    elif choix == "9":
        break
    else:
        print("Choix invalide.")

cursor.close()
conn.close()