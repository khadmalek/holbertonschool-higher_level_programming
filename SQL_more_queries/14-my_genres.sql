-- Sélectionner les noms de genres depuis tv_genres basés sur l'émission Dexter depuis tv_shows et tv_show_genres
-- Utiliser INNER JOIN pour lier tv_shows, tv_show_genres et tv_genres basés sur leurs IDs respectifs
-- Les résultats sont triés par nom de genre dans l'ordre croissant
SELECT 
    tv_genres.name
FROM 
    tv_shows
JOIN 
    tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN 
    tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE 
    tv_shows.title = 'Dexter'
ORDER BY 
    tv_genres.name ASC;
