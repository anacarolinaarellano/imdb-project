# The whole product
import json
import re

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

class MovieBuilder:
   def __init__(self, movie_title, year, place, star_cast, rating, link, preference_key):
      self.movie_title = movie_title
      self.year = year
      self.place = place
      self.star_cast = star_cast
      self.rating = rating
      self.link = link
      self.preference_key = preference_key
      self.vote=""

   def addVote(self, vote):
        self.vote = vote

   def build(self):
        movie = Movie(self)
        return movie
