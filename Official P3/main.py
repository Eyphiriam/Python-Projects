
from movie import Movie
from date import Date
from schedule import ReleaseSchedule
from movie_not_found_error import MovieNotFoundError

ACTION_1 = 1
ACTION_2 = 2
ACTION_3 = 3
ACTION_4 = 4
ACTION_5 = 5

studio_name = input("What is the name of your studio? ")
season_schedule = input("What season do you have a schedule for? ")
movie_choice = int(input("Enter 1 to add a movie, 2 to schedule a movie premiere, 3 to postpone a movie premiere, 4 for a summary, 5 to finish. "))
schedule = ReleaseSchedule(studio_name, season_schedule)

while movie_choice != ACTION_5:
    if movie_choice == ACTION_1:
        movie_name = input("Movie Name: ")
        movie_genre = input("Genre: ")
        item = Movie(movie_name, movie_genre)
        schedule.add_movie(item)
    if movie_choice == ACTION_2:
        movie_name = input("Movie Name: ")
        try:
            date = input("Date (mm-dd-yy): ")
        except:
            print("Could not find movie. Please try again.")
    if movie_choice == ACTION_3:
        movie_name = input("Movie Name: ")
        try:
            postpone = schedule.postpone_movie()
            print("Postponed to", postpone)
        except:
            print("Could not postpone movie. Please try again.")
    if movie_choice == ACTION_4:
        print(schedule.display_company_summary())
    movie_choice = float(input("Enter 1 to add a movie, 2 to schedule a movie premiere, 3 to postpone a movie premiere, 4 for a summary, 5 to finish. "))

print(schedule.display_schedule())
