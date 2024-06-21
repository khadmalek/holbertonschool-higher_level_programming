-- Ce script crée l'utilisateur du serveur MySQL user_0d_1 avec tous les privilèges
-- et définit le mot de passe sur user_0d_1_pwd.

-- Créer l'utilisateur si il n'existe pas
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Accorder tous les privilèges sur toutes les bases de données et tables
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Appliquer les changements
FLUSH PRIVILEGES;
