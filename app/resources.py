from flask_restful import Resource, abort
from app.parsers import film_parser, film_update_parser

FILMS = {
    'film1': {'name': 'Psycho', 'genres': ['Thriller', 'Mystery'], 'rating': 9.2, 'language': 'English'},
    'film2': {'name': 'Raid-Redemption', 'genres': ['Action'], 'rating': 8.8, 'language': 'English'},
    'film3': {'name': 'Kumbalangi Nights', 'genres': ['Romance', 'Drama'], 'rating': 9, 'language': 'Malayalam'},
}


def abort_if_film_doesnt_exist(film_id):
    """
        Abort request when either film_id does not exist
    """
    if film_id not in FILMS:
        abort(400, message="{} doesn't exists".format(film_id))


class Film(Resource):
    def get(self, film_id=None):
        """
            Return film details for the given film_id
        """
        abort_if_film_doesnt_exist(film_id)
        return FILMS[film_id]

    def put(self, film_id=None):
        """
            Update film details for the given film_id
        """
        abort_if_film_doesnt_exist(film_id)
        args = film_update_parser.parse_args()
        print(args)
        for key, value in args.items():
            if value:
                FILMS[film_id][key] = value
        return FILMS[film_id], 201

    def delete(self, film_id=None):
        """
            Delete film details for the given film_id
        """
        abort_if_film_doesnt_exist(film_id)
        del FILMS[film_id]
        return {'message': '{} deleted'.format(film_id)}, 204


class Films(Resource):
    def get(self):
        """
            Return all films
        """
        return FILMS

    def post(self):
        """
                Insert new film
            """
        # strict=True: raise 400 in case of any extra argument
        args = film_parser.parse_args(strict=True)
        film_id = int(max(FILMS.keys()).lstrip('film')) + 1
        film_id = 'film{}'.format(film_id)
        FILMS[film_id] = {
            'name': args['name'],
            'genres': args['genres'],
            'rating': args['rating'],
            'language': args['language'],
        }
        return FILMS[film_id], 201
