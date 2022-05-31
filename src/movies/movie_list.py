# The whole product
import json
import re

from movie_builder import MovieBuilder

# SOLID principle identified: Dependency inversion
class MovieList:
    def __init__(self, soup):
        #Get webpage information
        self.movies = soup.select('td.titleColumn')
        self.links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
        self.crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
        self.ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
        self.votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]

    def createMovieList(self):
        #Create movie list 
        self.list=[]
        for index in range(0, len(self.movies)):
            movie_string = self.movies[index].get_text()
            movie = (' '.join(movie_string.split()).replace('.', ''))
            movie_title = movie[len(str(index)) + 1:-7]
            year = re.search('\((.*?)\)', movie_string).group(1)
            place = movie[:len(str(index)) - (len(movie))]

            #Append json object
            movieBuilder = MovieBuilder(movie_title, year, place, self.crew[index], self.ratings[index], self.links[index], index % 4 + 1)
            if self.votes[index] != None:
                movieBuilder.addVote(self.votes[index])
            movieObj = movieBuilder.build()
            movieJson = movieObj.jsonFormat()
            self.list.append(movieJson)
        return self.list
