class Film():
	'''Film class ´that represent  each movie with the corresponding attributes'''
	def __init__(self, **kwargs):
		self.title = kwargs['title']
		self.release = kwargs['release']
		self.credits = kwargs['credits']
		self.notes = kwargs['notes']

	def __str__(self):
		return self.title

class Filmography(object):
	def __init__(self,data_file):
		self.__movie = []
		try:
			with open(data_file, 'r') as f:
				next(f)
				for line in f:
					dict_to_write = {}
					date, title, *credits, notes = line.split(';')
					dict_to_write['title'] = title
					dict_to_write['release'] = date
					dict_to_write['credits'] = self.__update_movie(credits)
					dict_to_write['notes'] = notes.strip() if len(notes) > 1 else 'No notes available'
					self.__movie.append(Movie(**dict_to_write))
		except IOError:
			print ('{} is an invalid filename!'.format(data_file))
			raise


	def __update_movie(self, credits_data):
		'''Populates credits for each film object '''
		credits = {}
		composer, producer, writer, director, role = credits_data
		credits['composer'] =  'Yes' if composer else 'No'
		credits['producer'] =  'Yes' if producer else 'No'
		credits['writer'] =  'Yes' if writer else 'No'
		credits['director'] =  'Yes' if director else 'No'
		credits['role'] = 'Yes' if role else 'No'
		return credits


	def __if_movie_exists(self,movie):
		'''Checks to see if the movie object exists or not
			and returns the movie object if exists'''
		movie = movie.lower()
		for each_movie in self.__movie:
			if each_movie.title.strip().lower() == movie:
				return each_movie
		return False

	def get_credits(self, movie):
		'''Find the credit for the given movie'''
		found_movie = self.__if_movie_exists(movie)
		if found_movie:
			return found_movie.credits
		return 'No movie with that name'

	def get_notes(self, movie):
		found_movie = self.__if_movie_exists(movie)
		if found_movie:
			return found_movie.notes
		return 'No movie found with that name'
			
	def get_release_date(self, movie='By the Sea'):
		'''Find the release date of a movie'''
		found_movie = self.__if_movie_exists(movie)
		if found_movie:
			return found_movie.release
		return 'No movie found with that name'
		
	def get_all_movies(self):
		'''Generates all of the movie objects '''
		for each_movie in self.__movie:
			yield each_movie

mv = Filmography('/resources/data/Filmography.txt')
print(mv.get_release_date('The Star Boarder'))
print(mv.get_credits('The Star Boarder'))

"""
#Unit tests
import unittest
class MyTest(unittest.TestCase):
	global mv 
	mv = Filmography('/resources/data/Filmography.txt')
	def test_get_credits(self):
		self.assertEqual(mv.get_release_date('A woman of paris'), '26-Sep-23')

	def test_length(self):
		movies = 0
		for movie in mv.get_all_movies():
			movies+=1
		self.assertEqual(len(mv.__movie), movies)


if __name__ =='_main_':
	unittest._main_()
"""
