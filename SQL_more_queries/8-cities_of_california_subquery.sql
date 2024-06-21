-- Sélectionner les villes de Californie sans utiliser JOIN
SELECT id, name 
FROM cities 
WHERE state_id = (SELECT id FROM states WHERE name = 'California') 
ORDER BY id ASC;
