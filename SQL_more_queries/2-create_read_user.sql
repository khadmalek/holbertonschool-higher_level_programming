-- Script pour créer la base de données hbtn_0d_2 et l'utilisateur user_0d_2 avec le privilège SELECT

-- Créer ou s'assurer de l'existence de la base de données hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Créer ou s'assurer de l'existence de l'utilisateur user_0d_2 et définir le mot de passe
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Accorder le privilège SELECT sur la base de données hbtn_0d_2 à user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Appliquer les changements
FLUSH PRIVILEGES;

