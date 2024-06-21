-- Tâche 9 : Créer la table second_table et insérer des lignes
-- Script SQL pour créer la table second_table et insérer des enregistrements

-- Créer la table second_table si elle n'existe pas
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Insérer les enregistrements dans second_table
INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10);
INSERT INTO second_table (id, name, score) VALUES (2, 'Alex', 3);
INSERT INTO second_table (id, name, score) VALUES (3, 'Bob', 14);
INSERT INTO second_table (id, name, score) VALUES (4, 'George', 8);
