-- Tâche 15 : Compter le nombre d'enregistrements avec le même score dans la table second_table
-- Script SQL pour compter les enregistrements avec le même score et les trier par nombre d'enregistrements décroissant

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
