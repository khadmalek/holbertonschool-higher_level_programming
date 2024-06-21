-- Sélectionner les titres des émissions de télévision depuis tv_shows basés sur le genre Comedy depuis tv_genres et tv_show_genres
-- Utiliser INNER JOIN pour lier tv_genres, tv_show_genres et tv_shows basés sur leurs IDs respectifs
-- Les résultats sont triés par titre de l'émission dans l'ordre croissant
SELECT 
    tv_shows.title
FROM 
    tv_genres
JOIN 
    tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN 
    tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE 
    tv_genres.name = 'Comedy'
ORDER BY 
    tv_shows.title ASC;
