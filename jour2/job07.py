import mysql.connector

class Employe:
    def __init__(self):
        self.connexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="entreprise"
        )
        self.curseur = self.connexion.cursor()

    # CREATE
    def ajouter(self, nom, prenom, salaire, id_service):
        requete = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        valeurs = (nom, prenom, salaire, id_service)
        self.curseur.execute(requete, valeurs)
        self.connexion.commit()
        print("Employé ajouté.")

    # READ
    def afficher_tous(self):
        self.curseur.execute("""
            SELECT employe.id, employe.nom, employe.prenom, employe.salaire, service.nom
            FROM employe
            JOIN service ON employe.id_service = service.id
        """)
        for emp in self.curseur.fetchall():
            print(emp)

    # UPDATE
    def modifier_salaire(self, id, nouveau_salaire):
        requete = "UPDATE employe SET salaire = %s WHERE id = %s"
        self.curseur.execute(requete, (nouveau_salaire, id))
        self.connexion.commit()
        print("Salaire mis à jour.")

    # DELETE
    def supprimer(self, id):
        requete = "DELETE FROM employe WHERE id = %s"
        self.curseur.execute(requete, (id,))
        self.connexion.commit()
        print("Employé supprimé.")

    def fermer(self):
        self.curseur.close()
        self.connexion.close()


#  Test du fonctionnement

if __name__ == "__main__":
    gestion = Employe()

    print("\n--- Liste des employés ---")
    gestion.afficher_tous()

    print("\n--- Ajout d'un employé ---")
    gestion.ajouter("Durand", "Paul", 3900, 1)

    print("\n--- Modification salaire ---")
    gestion.modifier_salaire(1, 3700)

    print("\n--- Suppression employé ---")
    gestion.supprimer(2)

    print("\n--- Liste finale ---")
    gestion.afficher_tous()

    gestion.fermer()