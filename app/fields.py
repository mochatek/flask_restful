from flask_restful import fields

"""
    Fields lets to filter and format response data
    attribute: allows to map output name to internal name
    Nested fields can be mapped like: fields.String(attribute='people_list.0.person_dictionary.name')
    default: In case data object dont have the attribute, we can specify default value to it like: fields.String(default='Guest')
"""

"""
    CUSTOM FORMATTING
    -----------------
    Subclass the 'fields.Raw' class and implement the format function.
"""


class Rating(fields.Raw):
    def format(self, value):
        return '{}/10'.format(value)


film_fields = {
    'id': fields.String(attribute='film_id'),
    'name': fields.String,
    'genres': fields.List(fields.String),
    'rating': Rating(attribute='rating'),
    'language': fields.String
}


# List of Nested objects
# film_list_fields = {
#     fields.List(fields.Nested(film_fields))
# }
