import fresh_tomatoes
import media

# instantiation of movie objects


buffalo_66 = media.Movie(
    "Buffalo 66", "Kidnapping and twisted revenge murders",
    "https://upload.wikimedia.org/wikipedia/en/thumb/b/b9/Buffalo_sixty_six_ver1.jpg/220px-Buffalo_sixty_six_ver1.jpg",  # noqa
    "https://www.youtube.com/watch?v=1duitd-N1Us")

midnight_cowboy = media.Movie(
    "Midnight Cowboy", "A hustling team in New York City",
    "https://upload.wikimedia.org/wikipedia/en/thumb/8/87/Midnight_Cowboy.jpg/220px-Midnight_Cowboy.jpg",  # noqa
    "https://www.youtube.com/watch?v=a2yBydiEJrI")

butch_sundance = media.Movie(
    "Butch Cassidy and the Sundance Kid", "Western bank robbers",
    "https://upload.wikimedia.org/wikipedia/en/thumb/f/fd/Butch_sundance_poster.jpg/220px-Butch_sundance_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=X41Ylp02NRs")

the_big_easy = media.Movie(
    "The Big Easy", "New Orleans crime thrillers",
    "https://upload.wikimedia.org/wikipedia/en/thumb/f/f4/Bigeasyposter.jpg/220px-Bigeasyposter.jpg",  # noqa
    "https://www.youtube.com/watch?v=SzWwINeiZa4")

white_men_cant_jump = media.Movie(
    "White Men Can't Jump", "Basketball Hustlers",
    "https://upload.wikimedia.org/wikipedia/en/thumb/6/6d/White_men_cant_jump.jpg/220px-White_men_cant_jump.jpg",  # noqa
    "https://www.youtube.com/watch?v=ebIGjo3Fzlc")

dope = media.Movie(
    "Dope", "Los Angeles crime-comedy thriller",
    "https://upload.wikimedia.org/wikipedia/en/d/d2/DopeTeaserPoster.jpg",
    "https://www.youtube.com/watch?v=sNlSBM8jVOY")

straight_outta_compton = media.Movie(
    "Straight Outta Compton", "N.W.A music biopic",
    "https://upload.wikimedia.org/wikipedia/en/thumb/7/7a/Straight_Outta_Compton_poster.jpg/220px-Straight_Outta_Compton_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=oyoew4T74_w")


the_force_awakens = media.Movie(
    "The Force Awakens", "Star Wars Episode VII",
    "https://upload.wikimedia.org/wikipedia/en/thumb/e/e6/Star_Wars_The_Force_Awakens_Teaser_Poster.jpg/220px-Star_Wars_The_Force_Awakens_Teaser_Poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=OMOVFvcNfvE")


# Selected movies are randomly sequenced and added to the entertaiment
# center page.
movies = [dope, straight_outta_compton, the_force_awakens,
          midnight_cowboy, buffalo_66, the_big_easy]
fresh_tomatoes.open_movies_page(movies)

# print(media.Movie.__module__)
