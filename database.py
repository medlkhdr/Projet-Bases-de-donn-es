import sqlite3

# Database connection function
def connect_db():
    return sqlite3.connect('hotel_db.sqlite')

# Function to retrieve all clients
def get_clients():
    query = "SELECT * FROM Client"
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(query)
        clients = cursor.fetchall()
        return clients
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return []
    finally:
        conn.close()

# Function to retrieve all reservations
def get_reservations():
    query = """
    SELECT R.id_Reservation, C.Nom_complet, H.Ville
    FROM Reservation R
    JOIN Client C ON R.id_Client = C.id_Client
    JOIN Concerner Co ON R.id_Reservation = Co.id_Reservation
    JOIN Type_Chambre T ON Co.id_Type = T.id_Type
    JOIN Chambre Ch ON T.id_Type = Ch.id_Type
    JOIN Hotel H ON Ch.id_Hotel = H.id_Hotel;
    """
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(query)
        reservations = cursor.fetchall()
        return reservations
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return []
    finally:
        conn.close()

# Function to retrieve available rooms based on dates
def get_available_rooms(start_date, end_date):
    query = """
    SELECT Ch.*
    FROM Chambre Ch
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
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(query, (start_date, end_date))
        rooms = cursor.fetchall()
        return rooms
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return []
    finally:
        conn.close()

# Function to add a client
def add_client(nom, adresse, ville, code_postal, email, telephone):
    query = """
    INSERT INTO Client (Nom_complet, Adresse, Ville, Code_postal, Email, Telephone)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(query, (nom, adresse, ville, code_postal, email, telephone))
        conn.commit()
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        conn.close()

# Function to add a reservation
def add_reservation(id_client, date_arrivee, date_depart):
    query = """
    INSERT INTO Reservation (id_Client, Date_arrivee, Date_depart)
    VALUES (?, ?, ?)
    """
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(query, (id_client, date_arrivee, date_depart))
        conn.commit()
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        conn.close()

