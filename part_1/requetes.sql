USE hotel_db;

-- a. Liste des réservations avec nom du client et ville de l’hôtel
SELECT R.id_Reservation, C.Nom_complet, H.Ville
FROM Reservation R
JOIN Client C ON R.id_Client = C.id_Client
JOIN Concerner Co ON R.id_Reservation = Co.id_Reservation
JOIN Type_Chambre T ON Co.id_Type = T.id_Type
JOIN Chambre Ch ON T.id_Type = Ch.id_Type
JOIN Hotel H ON Ch.id_Hotel = H.id_Hotel;

-- b. Clients habitant à Paris
SELECT * FROM Client WHERE Ville = 'Paris';

-- c. Nombre de réservations par client
SELECT C.Nom_complet, COUNT(R.id_Reservation) AS nb_reservations
FROM Client C
LEFT JOIN Reservation R ON C.id_Client = R.id_Client
GROUP BY C.id_Client;

-- d. Nombre de chambres par type
SELECT T.Type, COUNT(Ch.id_Chambre) AS nb_chambres
FROM Type_Chambre T
LEFT JOIN Chambre Ch ON T.id_Type = Ch.id_Type
GROUP BY T.id_Type;

-- e. Chambres non réservées entre deux dates (exemple entre 2025-06-10 et 2025-06-20)
SELECT Ch.*
FROM Chambre Ch
WHERE Ch.id_Chambre NOT IN (
  SELECT DISTINCT Ch.id_Chambre
  FROM Chambre Ch
  JOIN Type_Chambre T ON Ch.id_Type = T.id_Type
  JOIN Concerner Co ON T.id_Type = Co.id_Type
  JOIN Reservation R ON Co.id_Reservation = R.id_Reservation
  WHERE NOT (R.Date_depart < '2025-06-10' OR R.Date_arrivee > '2025-06-20')
);

