-- Tâche 11 : Lister les enregistrements avec score >= 10 dans la table second_table
-- Script SQL pour lister les enregistrements avec score >= 10, avec score et name, ordonnés par score décroissant

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
