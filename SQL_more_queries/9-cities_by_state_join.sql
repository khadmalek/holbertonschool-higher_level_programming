-- Sélectionner l'id, le nom des villes et le nom de l'État correspondant en utilisant une sous-requête
-- La sous-requête trouve le nom de l'État basé sur state_id dans la table cities
-- Les résultats sont ordonnés par cities.id dans l'ordre croissant
SELECT 
    cities.id, 
    cities.name, 
    (SELECT name FROM states WHERE states.id = cities.state_id) AS state_name
FROM 
    cities
ORDER BY 
    cities.id ASC;
