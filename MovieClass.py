import webbrowser


# Here we declare the Movie Class
class Movie():
"""This is the Movie object, which holds a title, storyline, and URLs for the poster and youtube trailer.
"""
   def __init__(self, movie_title, movie_storyline, movie_poster_image, movie_trailer_youtube):
       self.title = movie_title
       self.storyline = movie_storyline
       self.poster_image_url = movie_poster_image
       self.trailer_youtube_url = movie_trailer_youtube

	   
# Here we define the show trailer method
   def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)