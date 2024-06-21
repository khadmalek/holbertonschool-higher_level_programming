-- Sélectionner le titre des émissions de télévision et l'identifiant du genre depuis la table tv_show_genres
-- Utiliser LEFT JOIN pour inclure toutes les émissions même si elles n'ont pas de genre associé
-- Les résultats sont triés par tv_shows.title et tv_show_genres.genre_id dans l'ordre croissant
SELECT 
    tv_shows.title, 
    tv_show_genres.genre_id 
FROM 
    tv_shows 
LEFT JOIN 
    tv_show_genres ON tv_shows.id = tv_show_genres.show_id 
ORDER BY 
    tv_shows.title ASC, 
    tv_show_genres.genre_id ASC;
