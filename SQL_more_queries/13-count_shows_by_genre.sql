-- Compter le nombre d'émissions dans chaque genre
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS nombre_de_shows
FROM tv_genres
-- Joindre la table tv_genres avec la table tv_show_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.id
-- Inclure uniquement les genres qui ont au moins une émission
HAVING COUNT(tv_show_genres.show_id) > 0
-- Ordonner les résultats par le nombre d'émissions dans chaque genre, du plus au moins élevé
ORDER BY nombre_de_shows DESC;
