import MovieClass
import WorkNicCageTomatoes

# Below we define the ten instances of the Movie class that will be populating our web page.
goneInSixtySeconds = MovieClass.Movie(
	"Gone in 60 Seconds", 
	"A retired master car thief must come back to the industry and steal 50 \
	cars with his crew in one night to save his brother's life.", 
	"http://ia.media-imdb.com/images/M/MV5BMTIwMzExNDEwN15BMl5BanBnXkFtZTYwODMxMzg2._V1._SY209_CR1,0,140,209_.jpg", # no pep8
	"https://www.youtube.com/watch?v=o6AyAM1buQ8")

theRock = MovieClass.Movie(
	"The Rock", 
	"A mild-mannered chemist and an ex-con must lead the counterstrike when \
	a rogue group of military men, led by a renegade general, threaten a nerve\
	gas attack from Alcatraz against San Francisco.",
	"http://ia.media-imdb.com/images/M/MV5BMTM3MTczOTM1OF5BMl5BanBnXkFtZTYwMjc1NDA5._V1._SY209_CR3,0,140,209_.jpg", # no pep8
	"https://www.youtube.com/watch?v=ClOQJAB0uD0")

nationalTreasure = MovieClass.Movie(
	"National Treasure", 
	"A historian races to find the legendary Templar Treasure before a team of mercenaries.",
	"http://ia.media-imdb.com/images/M/MV5BMTY3NTc4OTYxMF5BMl5BanBnXkFtZTcwMjk5NzUyMw@@._V1._SY209_CR0,0,140,209_.jpg", # no pep8
	"https://www.youtube.com/watch?v=mcf4tXYjaxo")

faceOff = MovieClass.Movie(
	"Face/Off", 
	"To foil an extortion plot, an FBI agent undergoes a face-transplant surgery \
	and assumes the identity of a ruthless terrorist. But the plan backfires when \
	the same criminal impersonates the cop with the same method.",
	"http://ia.media-imdb.com/images/M/MV5BMTU4MjA5NTc2NV5BMl5BanBnXkFtZTgwOTI2Mzk5MDE@._V1._SX140_CR0,0,140,209_.jpg", # no pep8
	"https://www.youtube.com/watch?v=Vlg-VRc6TbY")

theFamilyMan = MovieClass.Movie(
	"The Family Man", 
	"A fast-lane investment broker, offered the opportunity to see how the other half \
	lives, wakes up to find that his sports car and girlfriend have become a mini-van and wife.",
	"http://ia.media-imdb.com/images/M/MV5BMTI2Mjc0MDYyOV5BMl5BanBnXkFtZTcwMzA5MDQyMQ@@._V1._SY209_CR5,0,140,209_.jpg", # no pep8 
	"https://www.youtube.com/watch?v=OnouJoQs52c")

ghostRider = MovieClass.Movie(
	"Ghost Rider", 
	"Stunt motorcyclist Johnny Blaze gives up his soul to become a hellblazing vigilante, \
	to fight against power hungry Blackheart, the son of the devil himself.",
	"http://ia.media-imdb.com/images/M/MV5BMzIyNDE5ODI1OV5BMl5BanBnXkFtZTcwNTIyNDE0MQ@@._V1._SY209_CR0,0,140,209_.jpg", # no pep8
	"https://www.youtube.com/watch?v=L-WTmTOi0zU")

theSorcerersApprentice = MovieClass.Movie(
	"The Sorcerer's Apprentice", 
	"Master sorcerer Balthazar Blake must find and train Merlin's descendant to defeat dark \
	sorceress Morgana le Fey.",
	"http://ia.media-imdb.com/images/M/MV5BNDY3NzQ0NjYxM15BMl5BanBnXkFtZTcwMDkzODM2Mw@@._V1._SY209_CR1,0,140,209_.jpg", # no pep8 
	"https://www.youtube.com/watch?v=v2uV0_1C4UM")

lordOfWar = MovieClass.Movie(
	"Lord of War", 
	"An arms dealer confronts the morality of his work as he is being chased by an Interpol agent.",
	"http://ia.media-imdb.com/images/M/MV5BMjEzNDM2OTgzN15BMl5BanBnXkFtZTcwMzU3MTIzMQ@@._V1._SY209_CR0,0,140,209_.jpg", # no pep8
	"https://www.youtube.com/watch?v=Ej83QvHuiNI")

badLieutenant = MovieClass.Movie(
	"Bad Lieutenant: Port of Call New Orleans", 
	"Terence McDonagh is a drug- and gambling-addled detective in post-Katrina New Orleans \ 
	investigating the killing of five Senegalese immigrants.",
	"http://ia.media-imdb.com/images/M/MV5BMTcyMzY0NTMzMF5BMl5BanBnXkFtZTcwMTc1MjY4Mg@@._V1._SY209_CR0,0,140,209_.jpg", # no pep8 
	"https://www.youtube.com/watch?v=2N5UcZJHy4g")

nextMovie = MovieClass.Movie(
	"Next", 
	"A Las Vegas magician who can see into the future is pursued by FBI agents seeking \
	to use his abilities to prevent a nuclear terrorist attack.",
	"http://ia.media-imdb.com/images/M/MV5BMTg3MjgyNjE1Nl5BMl5BanBnXkFtZTcwNTY1NDU0MQ@@._V1._SY209_CR0,0,140,209_.jpg", # no pep8 
	"https://www.youtube.com/watch?v=rIlka-7WLnQ")

# Here we place the instances of the movie class into an array	
movieList = [goneInSixtySeconds, theRock, nationalTreasure, faceOff, theFamilyMan, ghostRider, 
	theSorcerersApprentice, lordOfWar, badLieutenant, nextMovie]

# We call the function to generate the web page, feeding in the array of Movie class instances
WorkNicCageTomatoes.open_movies_page(movieList)
