-- Tâche 16 : Lister tous les enregistrements avec un nom dans la table second_table
-- Script SQL pour lister les enregistrements avec un nom et trier par score décroissant

SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name <> ''
ORDER BY score DESC;
