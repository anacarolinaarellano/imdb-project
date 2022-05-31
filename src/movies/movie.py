# The whole product
import json
import re

# SOLID principle identified: Single Responsibility
class Movie:
   def __init__(self, movie):
      self.movie_title = movie.movie_title
      self.year = movie.year
      self.place = movie.place
      self.star_cast = movie.star_cast
      self.rating = movie.rating
      self.link = movie.link
      self.preference_key = movie.preference_key

   def jsonFormat(self):
        jsonStr = json.dumps(self.__dict__)
        myJson = json.loads(jsonStr)
        return myJson
