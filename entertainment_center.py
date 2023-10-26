import media
from fresh_tomatoes import *

toy_story = media.Movie("Toy Story",
						"A story of a boy and his toys that come to life",
						"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"https://www.youtube.com/watch?v=vwyZH85NQC4")

# print(toy_story.story_line)
# toy_story.show_trailer()

avatar=media.Movie ("Avatar",
					"A marine on an alien planet",
					"http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
					"https://www.youtube.com/watch?v=5PSNL1qE6VY")


school_of_rock=media.Movie ("School of Rock",
							"Using rock music to learn",
							"http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
							"https://www.youtube.com/watch?v=3PSUJFEBC74")

movies = [avatar, toy_story, school_of_rock]
# fresh_tomatoes.open(movies)
open_movies_page(movies)