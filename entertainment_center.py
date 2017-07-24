import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=-9ceBgWV8io")

good_will_hunting = media.Movie("Good Will Hunting",
                                "https://upload.wikimedia.org/wikipedia/en/b/b8/Good_Will_Hunting_theatrical_poster.jpg",
                                "https://www.youtube.com/watch?v=PaZVjZEFkRs")

hitch = media.Movie("Hitch",
                    "https://upload.wikimedia.org/wikipedia/en/d/d4/Hitch_poster.JPG",
                    "https://www.youtube.com/watch?v=dMaq_pfxs-0")

school_of_rock = media.Movie("School of Rock",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=atLg2wQQxvU")

hunger_games = media.Movie("Hunger Games",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=PbA637H0bo")

the_martian = media.Movie("The Martian",
                           "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",
                           "https://www.youtube.com/watch?v=Ue4PCI0NamI")

movies = [toy_story, avatar, good_will_hunting, hitch, school_of_rock, ratatouille, midnight_in_paris, hunger_games,
          the_martian]

fresh_tomatoes.open_movies_page(movies)
