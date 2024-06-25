from movie import Movie
from date import Date
from movie_not_found_error import MovieNotFoundError


class ReleaseSchedule:

    movie_picked = False # in order for movie_chosen to work in schedule_movie

    def __init__(self, studio_name: str, season: str):
        self.studio_name = studio_name
        self.season = season
        self.movie_list = []
        self.schedule = {}


    def add_movie(self, movie: Movie) -> None:
        self.movie_list.append(movie)
        

    def schedule_movie(self, movie_title: str, date: Date) -> None:
        for object in self.movie_list:
            if movie_title == object.title:
                movie_picked = True
        if movie_picked == True:
            self.schedule[movie_title] = date
        else:
            raise MovieNotFoundError("Could not postpone movie. Please try again.")

    def postpone_movie(self, movie_title: str) -> Date:
        if movie_title in self.schedule:
            preimere_date = self.schedule[movie_title]
            preimere_date.year += 1
            self.schedule[movie_title] = preimere_date
            return preimere_date
        else:
            raise MovieNotFoundError("Could not postpone movie. Please try again.")


    def display_company_summary(self) -> None:
        print(self.studio_name)
        if len(self.movie_list) == len(self.schedule):
            print("{}: {} movie premieres".format(self.season, len(self.movie_list)))
        else:
            print("{}: {} movie premieres ({} to be scheduled)".format(self.season, len(self.movie_list), (len(self.movie_list) - len(self.schedule))))

    
    def display_schedule(self) -> None:
        for movie in self.movie_list:
            date = self.schedule[movie]
            if movie in self.schedule:
                print(movie)
                print(date)
            else:
                print("{}\n".format(movie) + "To Be Schedule")
