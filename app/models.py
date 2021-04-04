class Movie:
    def __init__(self, film_id, name, genres, rating, language):
        """
        Initialize movie properties
            :param str filmID: ID of the film
            :param str name: Name of the film
            :param list genres: Genres of the film
            :param float rating: Rating of the film
            :param str language: Language of the film
        """
        self.film_id = film_id
        self.name = name
        self.genres = genres
        self.rating = rating
        self.language = language

    def update(self, name, genres, rating, language):
        """
        Update movie properties if not None
        """
        if name:
            self.name = name
        if genres:
            self.genres = genres
        if rating:
            self.rating = rating
        if language:
            self.language = language
