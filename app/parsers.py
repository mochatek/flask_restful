from flask_restful import reqparse
# Access variables in flask.request object

"""
    trim: removes white space from the arguments
    bundle_errors: bundle all the errors into a dict. If false abort at first failure
"""

film_parser = reqparse.RequestParser(trim=True, bundle_errors=True)

"""
    help: Error message.
    error_msg can be used for interpolation
    action='append' for list if location=form
    type is string by default
    default: default value
    choices: possible values
"""

film_parser.add_argument('name', required=True,
                         help='Name cannot be blank')

film_parser.add_argument('genres', type=list, required=True,
                         help='Genre cannot be empty', location='json')

film_parser.add_argument('rating', type=float, required=True,
                         help='Incorrect rating: {error_msg}')

film_parser.add_argument('language', required=True, choices=('English', 'Malayalam'),
                         help='Incorrect language: {error_msg}')

"""
    By default, the RequestParser tries to parse values from flask.Request.values, and flask.Request.json.
    location: specify alternate locations (POST body, querystring, headers, cookies, file uploads)
    for list arguments, use type=list when location='json'
    for multiple locations, use [] => location=['headers', 'values']
"""
# parser.add_argument('name', type=int, location='form')
# parser.add_argument('PageSize', type=int, location='args')
# parser.add_argument('User-Agent', location='headers')
# parser.add_argument('session_id', location='cookies')
# parser.add_argument('picture', type=werkzeug.datastructures.FileStorage, location='files')


"""
    PARSER INHERITANCE
    ------------------
    extend parser with copy()
    overwrite any argument with replace_argument()
    remove argument completely with remove_argument()
"""
# parser = reqparse.RequestParser()
# parser.add_argument('foo', type=int)

# parser_copy = parser.copy()
# parser_copy.add_argument('bar', type=int)

# parser_copy.replace_argument('foo', required=True, location='json')

# parser_copy.remove_argument('foo')

film_update_parser = film_parser.copy()
film_update_parser.replace_argument('name', required=False)
film_update_parser.replace_argument('genres', required=False)
film_update_parser.replace_argument('rating', required=False)
film_update_parser.replace_argument('language', required=False)
