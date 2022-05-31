from movie import Movie

# DEDIGN PATTERN IMPLEMENTED: BUILDER
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