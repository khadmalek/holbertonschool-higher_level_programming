-- Script pour créer la table unique_id si elle n'existe pas

-- Vérifier si la table unique_id existe
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);

-- Cette ligne garantit que la table aura les deux colonnes et leurs exigences
