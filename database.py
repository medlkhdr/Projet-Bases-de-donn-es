# database.py amélioré avec fonctionnalités supplémentaires
import sqlite3

# Connexion à la base de données

def connexion_db():
    return sqlite3.connect("hotel_db.sqlite")

# Obtenir la liste des clients

def obtenir_clients():
    try:
        conn = connexion_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Client")
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Erreur SQLite: {e}")
        return []
    finally:
        conn.close()

# Obtenir les réservations avec détails du client et de l'hôtel

def obtenir_reservations():
    query = """
    SELECT R.id_Reservation, C.Nom_complet, C.Email, R.Date_arrivee, R.Date_depart, H.Ville, H.Pays
    FROM Reservation R
    JOIN Client C ON R.id_Client = C.id_Client
    JOIN Concerner Co ON R.id_Reservation = Co.id_Reservation
    JOIN Type_Chambre T ON Co.id_Type = T.id_Type
    JOIN Chambre Ch ON T.id_Type = Ch.id_Type
    JOIN Hotel H ON Ch.id_Hotel = H.id_Hotel;
    """
    try:
        conn = connexion_db()
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Erreur SQLite: {e}")
        return []
    finally:
        conn.close()

# Obtenir les chambres disponibles entre deux dates

def obtenir_chambres_disponibles(date_debut, date_fin):
    query = """
    SELECT Ch.id_Chambre, Ch.Numero, Ch.Etage, Ch.Fumeurs, H.Ville, T.Type, T.Tarif
    FROM Chambre Ch
    JOIN Hotel H ON Ch.id_Hotel = H.id_Hotel
    JOIN Type_Chambre T ON Ch.id_Type = T.id_Type
    WHERE Ch.id_Chambre NOT IN (
        SELECT DISTINCT Ch.id_Chambre
        FROM Chambre Ch
        JOIN Type_Chambre T ON Ch.id_Type = T.id_Type
        JOIN Concerner Co ON T.id_Type = Co.id_Type
        JOIN Reservation R ON Co.id_Reservation = R.id_Reservation
        WHERE NOT (R.Date_depart < ? OR R.Date_arrivee > ?)
    );
    """
    try:
        conn = connexion_db()
        cursor = conn.cursor()
        cursor.execute(query, (date_debut, date_fin))
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Erreur SQLite: {e}")
        return []
    finally:
        conn.close()

# Ajouter un nouveau client

def ajouter_client(nom, adresse, ville, code_postal, email, telephone):
    query = """
    INSERT INTO Client (Nom_complet, Adresse, Ville, Code_postal, Email, Telephone)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    try:
        conn = connexion_db()
        cursor = conn.cursor()
        cursor.execute(query, (nom, adresse, ville, code_postal, email, telephone))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Erreur SQLite: {e}")
    finally:
        conn.close()

# Ajouter une réservation avec une chambre (fonctionnalité étendue)

def ajouter_reservation(id_client, date_arrivee, date_depart, id_type):
    try:
        conn = connexion_db()
        cursor = conn.cursor()
        # Insérer la réservation
        cursor.execute("""
            INSERT INTO Reservation (id_Client, Date_arrivee, Date_depart)
            VALUES (?, ?, ?)
        """, (id_client, date_arrivee, date_depart))
        reservation_id = cursor.lastrowid

        # Ajouter dans la table Concerner
        cursor.execute("""
            INSERT INTO Concerner (id_Reservation, id_Type)
            VALUES (?, ?)
        """, (reservation_id, id_type))

        conn.commit()
    except sqlite3.Error as e:
        print(f"Erreur SQLite: {e}")
    finally:
        conn.close()

# Obtenir la liste des villes d'hôtels pour filtrage (fonctionnalité UI)

def obtenir_villes_hotels():
    query = "SELECT DISTINCT Ville FROM Hotel"
    try:
        conn = connexion_db()
        cursor = conn.cursor()
        cursor.execute(query)
        return [row[0] for row in cursor.fetchall()]
    except sqlite3.Error as e:
        print(f"Erreur SQLite: {e}")
        return []
    finally:
        conn.close()

# Obtenir les types de chambres pour le formulaire de réservation

def obtenir_types_chambres():
    query = "SELECT id_Type, Type, Tarif FROM Type_Chambre"
    try:
        conn = connexion_db()
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Erreur SQLite: {e}")
        return []
    finally:
        conn.close()

