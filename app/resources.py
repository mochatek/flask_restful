from flask_restful import Resource, abort, marshal_with
from app.parsers import film_parser, film_update_parser
from app.models import Movie
from app.fields import film_fields
from functools import wraps


def cache(f):
    @wraps(f)
    def cacher(*args, **kwargs):
        # caching stuff
        pass
    return cacher


FILMS = [
    Movie('film1', 'Psycho', ['Thriller', 'Mystery'], 9.2, 'English'),
    Movie('film2', 'Raid-Redemption', ['Action'], 8.8, 'English'),
    Movie('film3', 'Kumbalangi Nights', ['Romance', 'Drama'], 9, 'Malayalam')
]


def find_film(film_id):
    """
        Retrieve film with film_id from films if present, else return None
    """
    film = list(filter(lambda f: f.film_id == film_id, FILMS))
    if len(film):
        return film[0]
    else:
        return None


# marshal_with decorator is used to fomat the reponse data with specified output field format
# envelope: attribute used as key of the result


class Film(Resource):
    # Decorators can be specified here in list, will be applied to all methods and inherited resources
    method_decorators = [cache]

    # Alternatively, you can specify a dictionary of iterables that map to HTTP methods and the decorators
    # will only apply to matching requests.
    method_decorators = {'get': [cache]}

    @marshal_with(film_fields)
    def get(self, film_id=None):
        """
            Return film details for the given film_id
        """
        film = find_film(film_id)
        if not film:
            abort(400, message="{} doesn't exists".format(film_id))

        return film

    @marshal_with(film_fields)
    def put(self, film_id=None):
        """
            Update film details for the given film_id
        """
        film = find_film(film_id)
        if not film:
            abort(400, message="{} doesn't exists".format(film_id))

        args = film_update_parser.parse_args()
        film.update(args['name'], args['genres'],
                    args['rating'], args['language'])
        return film, 201

    def delete(self, film_id=None):
        """
            Delete film details for the given film_id
        """
        film = find_film(film_id)
        if not film:
            abort(400, message="{} doesn't exists".format(film_id))

        FILMS.remove(film)
        return {'message': '{} deleted'.format(film_id)}, 200


class Films(Resource):
    @marshal_with(film_fields)
    def get(self):
        """
            Return all films
        """
        return FILMS

    @marshal_with(film_fields)
    def post(self):
        """
                Insert new film
            """
        # strict=True: raise 400 in case of any extra argument
        args = film_parser.parse_args(strict=True)
        film_id = 'film{}'.format(
            max(list(map(lambda f: int(f.film_id.lstrip('film')), FILMS))) + 1)
        film = Movie(film_id, args['name'], args['genres'],
                     args['rating'], args['language'])
        FILMS.append(film)
        return film, 201
