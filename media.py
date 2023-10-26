import webbrowser

class Movie():
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.story_line = movie_storyline
		self.poster_image_url = poster_image
		# Here trailer url only support the youtube url, because the html generator class use some 
		# js code to fit for the youtube url only.
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)