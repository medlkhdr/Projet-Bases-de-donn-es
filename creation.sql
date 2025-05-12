DROP TABLE IF EXISTS Concerner;
DROP TABLE IF EXISTS Offre;
DROP TABLE IF EXISTS Evaluation;
DROP TABLE IF EXISTS Reservation;
DROP TABLE IF EXISTS Chambre;
DROP TABLE IF EXISTS Type_Chambre;
DROP TABLE IF EXISTS Prestation;
DROP TABLE IF EXISTS Client;
DROP TABLE IF EXISTS Hotel;

CREATE TABLE Hotel (
  id_Hotel INTEGER PRIMARY KEY,
  Ville TEXT NOT NULL,
  Pays TEXT NOT NULL,
  Code_postal TEXT NOT NULL
);

CREATE TABLE Client (
  id_Client INTEGER PRIMARY KEY,
  Adresse TEXT NOT NULL,
  Ville TEXT NOT NULL,
  Code_postal TEXT NOT NULL,
  Email TEXT NOT NULL,
  Telephone TEXT NOT NULL,
  Nom_complet TEXT NOT NULL
);

CREATE TABLE Prestation (
  id_Prestation INTEGER PRIMARY KEY,
  Prix REAL NOT NULL,
  Description TEXT NOT NULL
);

CREATE TABLE Type_Chambre (
  id_Type INTEGER PRIMARY KEY,
  Type TEXT NOT NULL,
  Tarif REAL NOT NULL
);

CREATE TABLE Chambre (
  id_Chambre INTEGER PRIMARY KEY,
  Numero INTEGER NOT NULL,
  Etage INTEGER NOT NULL,
  Fumeurs BOOLEAN NOT NULL,
  id_Hotel INTEGER NOT NULL,
  id_Type INTEGER NOT NULL,
  FOREIGN KEY (id_Hotel) REFERENCES Hotel(id_Hotel),
  FOREIGN KEY (id_Type) REFERENCES Type_Chambre(id_Type)
);

CREATE TABLE Reservation (
  id_Reservation INTEGER PRIMARY KEY,
  Date_arrivee DATE NOT NULL,
  Date_depart DATE NOT NULL,
  id_Client INTEGER NOT NULL,
  FOREIGN KEY (id_Client) REFERENCES Client(id_Client)
);

CREATE TABLE Evaluation (
  id_Evaluation INTEGER PRIMARY KEY,
  Date_arrivee DATE NOT NULL,
  Note INTEGER NOT NULL,
  Texte TEXT,
  id_Client INTEGER NOT NULL,
  FOREIGN KEY (id_Client) REFERENCES Client(id_Client)
);

CREATE TABLE Offre (
  id_Hotel INTEGER,
  id_Prestation INTEGER,
  PRIMARY KEY (id_Hotel, id_Prestation),
  FOREIGN KEY (id_Hotel) REFERENCES Hotel(id_Hotel),
  FOREIGN KEY (id_Prestation) REFERENCES Prestation(id_Prestation)
);

CREATE TABLE Concerner (
  id_Reservation INTEGER,
  id_Type INTEGER,
  PRIMARY KEY (id_Reservation, id_Type),
  FOREIGN KEY (id_Reservation) REFERENCES Reservation(id_Reservation),
  FOREIGN KEY (id_Type) REFERENCES Type_Chambre(id_Type)
);

