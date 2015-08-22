import fresh_tomatoes
import media


toy_story = media.Movie("Toy Story",
                       "A story of a boy and his toys that come to life.",
                       "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                       "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")


buffalo_66 = media.Movie("Buffalo 66",
                     "Kidnapping and twisted revenge murder",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b9/Buffalo_sixty_six_ver1.jpg/220px-Buffalo_sixty_six_ver1.jpg",
                     "https://www.youtube.com/watch?v=1duitd-N1Us")

school_of_rock = media.Movie("School of Rock",
                     "Using rock music to learn",
                     "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                     "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille",
                     "A rat is a chef in Paris",
                     "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                     "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
                     "Going back in time to meet authors",
                     "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                     "https://www.youtube.com/watch?v=5nOF93SzX6s")

hunger_games = media.Movie("Hunger Games",
                     "A really real reality show",
                     "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                     "https://www.youtube.com/watch?v=PbA63a1H0bo")

midnight_cowboy = media.Movie("Midnight Cowboy",
                     "A hustling team in New York City",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/8/87/Midnight_Cowboy.jpg/220px-Midnight_Cowboy.jpg",
                     "https://www.youtube.com/watch?v=a2yBydiEJrI")

butch_sundance = media.Movie("Butch Cassidy and the Sundance Kid",
                     "Western bank robbers",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/f/fd/Butch_sundance_poster.jpg/220px-Butch_sundance_poster.jpg",
                     "https://www.youtube.com/watch?v=X41Ylp02NRs")

empire_strikes_back = media.Movie("The Empire Strikes Back",
                     "Continuing the Star Wars saga",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/3/3c/SW_-_Empire_Strikes_Back.jpg/220px-SW_-_Empire_Strikes_Back.jpg",
                     "https://www.youtube.com/watch?v=96v4XraJEPI")

the_big_easy = media.Movie("The Big Easy",
                     "New Orleans crime thriller",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/f/f4/Bigeasyposter.jpg/220px-Bigeasyposter.jpg",
                     "https://www.youtube.com/watch?v=SzWwINeiZa4")

white_men_cant_jump = media.Movie("White Men Can't Jump",
                     "Basketball Hustlers",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/6/6d/White_men_cant_jump.jpg/220px-White_men_cant_jump.jpg",
                     "https://www.youtube.com/watch?v=ebIGjo3Fzlc")



movies = [white_men_cant_jump, the_big_easy, empire_strikes_back, butch_sundance, midnight_cowboy, buffalo_66]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.__module__)
