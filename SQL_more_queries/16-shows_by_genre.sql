-- Sélectionner le titre des émissions de télévision et leurs genres correspondants depuis tv_shows, tv_genres et tv_show_genres
-- Utiliser LEFT JOIN pour inclure toutes les émissions depuis tv_shows et faire correspondre les genres depuis tv_show_genres et tv_genres
-- Les résultats sont triés par titre de l'émission et nom du genre dans l'ordre croissant
SELECT 
    tv_shows.title,
    tv_genres.name
FROM 
    tv_shows
LEFT JOIN 
    tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN 
    tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY 
    tv_shows.title ASC, tv_genres.name ASC;
