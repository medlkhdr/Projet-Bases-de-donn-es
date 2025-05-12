CREATE DATABASE IF NOT EXISTS hotel_db CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE hotel_db;

CREATE TABLE Hotel (
  id_Hotel INT PRIMARY KEY,
  Ville VARCHAR(100) NOT NULL,
  Pays VARCHAR(100) NOT NULL,
  Code_postal VARCHAR(10) NOT NULL
);

CREATE TABLE Client (
  id_Client INT PRIMARY KEY,
  Adresse VARCHAR(255) NOT NULL,
  Ville VARCHAR(100) NOT NULL,
  Code_postal VARCHAR(10) NOT NULL,
  Email VARCHAR(255) NOT NULL,
  Telephone VARCHAR(20) NOT NULL,
  Nom_complet VARCHAR(150) NOT NULL
);

CREATE TABLE Prestation (
  id_Prestation INT PRIMARY KEY,
  Prix DECIMAL(8,2) NOT NULL,
  Description VARCHAR(255) NOT NULL
);

CREATE TABLE Type_Chambre (
  id_Type INT PRIMARY KEY,
  Type VARCHAR(50) NOT NULL,
  Tarif DECIMAL(8,2) NOT NULL
);

CREATE TABLE Chambre (
  id_Chambre INT PRIMARY KEY,
  Numero INT NOT NULL,
  Etage INT NOT NULL,
  Fumeurs BOOLEAN NOT NULL,
  id_Hotel INT NOT NULL,
  id_Type INT NOT NULL,
  FOREIGN KEY (id_Hotel) REFERENCES Hotel(id_Hotel),
  FOREIGN KEY (id_Type) REFERENCES Type_Chambre(id_Type)
);

CREATE TABLE Reservation (
  id_Reservation INT PRIMARY KEY,
  Date_arrivee DATE NOT NULL,
  Date_depart DATE NOT NULL,
  id_Client INT NOT NULL,
  FOREIGN KEY (id_Client) REFERENCES Client(id_Client)
);

CREATE TABLE Evaluation (
  id_Evaluation INT PRIMARY KEY,
  Date_arrivee DATE NOT NULL,
  Note TINYINT NOT NULL,
  Texte TEXT,
  id_Client INT NOT NULL,
  FOREIGN KEY (id_Client) REFERENCES Client(id_Client)
);

CREATE TABLE Offre (
  id_Hotel INT,
  id_Prestation INT,
  PRIMARY KEY (id_Hotel, id_Prestation),
  FOREIGN KEY (id_Hotel) REFERENCES Hotel(id_Hotel),
  FOREIGN KEY (id_Prestation) REFERENCES Prestation(id_Prestation)
);

CREATE TABLE Concerner (
  id_Reservation INT,
  id_Type INT,
  PRIMARY KEY (id_Reservation, id_Type),
  FOREIGN KEY (id_Reservation) REFERENCES Reservation(id_Reservation),
  FOREIGN KEY (id_Type) REFERENCES Type_Chambre(id_Type)
);

