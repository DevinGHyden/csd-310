def show_films(cursor, label):
    print(f"\n-- {label} --")
    query = ("SELECT film_name AS Name, film_director AS Director, "
             "genre_name AS Genre, studio_name AS Studio "
             "FROM film INNER JOIN genre ON film.genre_id = genre.genre_id "
             "INNER JOIN studio ON film.studio_id = studio.studio_id")
    cursor.execute(query)
    for (Name, Director, Genre, Studio) in cursor.fetchall():
        print(f"Name: {Name} | Director: {Director} | Genre: {Genre} | Studio: {Studio}")