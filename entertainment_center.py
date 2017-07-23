import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar_Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=-9ceBgWV8io")

print(avatar.storyline)

good_will_hunting = media.Movie("Good Will Hunting",
                                "A story about a gifted but troubled young man and an MIT professor "
                                "who decides to help the misguided youth reach his potential",
                                "https://en.wikipedia.org/wiki/Good_Will_Hunting#/media/File:"
                                "Good_Will_Hunting_theatrical_poster.jpg",
                                "https://www.youtube.com/watch?v=PaZVjZEFkRs")

print(good_will_hunting.storyline)

hitch = media.Movie("Hitch",
                    "A movie about a 'date doctor' who coaches other men in the art of wooing women, "
                    "with a focus on long-term relationships.",
                    "https://en.wikipedia.org/wiki/Hitch_(film)#/media/File:Hitch_poster.JPG",
                    "https://www.youtube.com/watch?v=dMaq_pfxs-0")

school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille",
                          "A rat is a chef in Paris",
                          "http://upload.wikimedia.org/wikipedia/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "Going back in time to meet authors",
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_poster.jpg",
                                "https://www.youtube.com/watch?v=atLg2wQQxvU")

hunger_games = media.Movie("Hunger Games",
                           "A really real reality show",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=PbA637H0bo")

movies = [toy_story, avatar, good_will_hunting, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
