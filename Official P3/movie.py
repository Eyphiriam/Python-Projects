class Movie:

    def __init__(self, movie_title: str, genre: str):
        self.movie_title = movie_title
        self.genre = genre
    
    def __str__(self) -> str:
        return f"Movie Name: {self.title}\nGenre: {self.genre}"