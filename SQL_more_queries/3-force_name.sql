-- Script pour créer la table force_name si elle n'existe pas

-- Vérifier si la table force_name existe
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
