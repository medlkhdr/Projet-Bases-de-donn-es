# database.py
import sqlite3

DB_NAME = "hotel_db.sqlite"

def connexion_db():
    return sqlite3.connect(DB_NAME)

def obtenir_clients():
    try:
        with connexion_db() as conn:
            return conn.execute("SELECT * FROM Client").fetchall()
    except sqlite3.Error as e:
        print(f"Erreur SQLite: {e}")
        return []

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
        with connexion_db() as conn:
            return conn.execute(query).fetchall()
    except sqlite3.Error as e:
        print(f"Erreur SQLite: {e}")
        return []

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
        with connexion_db() as conn:
            return conn.execute(query, (date_debut, date_fin)).fetchall()
    except sqlite3.Error as e:
        print(f"Erreur SQLite: {e}")
        return []

def ajouter_client(nom, adresse, ville, code_postal, email, telephone):
    query = """
    INSERT INTO Client (Nom_complet, Adresse, Ville, Code_postal, Email, Telephone)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    try:
        with connexion_db() as conn:
            conn.execute(query, (nom, adresse, ville, code_postal, email, telephone))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Erreur SQLite: {e}")

def ajouter_reservation(id_client, date_arrivee, date_depart, id_type):
    try:
        with connexion_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Reservation (id_Client, Date_arrivee, Date_depart)
                VALUES (?, ?, ?)
            """, (id_client, date_arrivee, date_depart))
            reservation_id = cursor.lastrowid

            cursor.execute("""
                INSERT INTO Concerner (id_Reservation, id_Type)
                VALUES (?, ?)
            """, (reservation_id, id_type))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Erreur SQLite: {e}")

def obtenir_types_chambres():
    try:
        with connexion_db() as conn:
            return conn.execute("SELECT id_Type, Type, Tarif FROM Type_Chambre").fetchall()
    except sqlite3.Error as e:
        print(f"Erreur SQLite: {e}")
        return []

