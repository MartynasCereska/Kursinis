# theater.py
class Movie:
    def __init__(self, title, genre, duration):
        self.title = title
        self.genre = genre
        self.duration = duration

    def __str__(self):
        return f"{self.title} ({self.genre}) - {self.duration} mins"

class Ticket:
    def __init__(self, movie, seat_number):
        self.movie = movie
        self.seat_number = seat_number

    def __str__(self):
        return f"Ticket for {self.movie.title}, Seat {self.seat_number}"

class TicketFactory:
    @staticmethod
    def create_ticket(movie, seat_number):
        return Ticket(movie, seat_number)

class Theater:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Theater, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.movies = []
            self.initialized = True

    def add_movie(self, movie):
        self.movies.append(movie)

    def show_movies(self):
        for movie in self.movies:
            print(movie)

    def export_movies_to_txt(self, filename):
        with open(filename, 'w') as file:
            for movie in self.movies:
                file.write(f"{movie.title},{movie.genre},{movie.duration}\n")

    @classmethod
    def import_movies_from_txt(cls, filename):
        theater = cls()
        with open(filename, 'r') as file:
            for line in file:
                title, genre, duration = line.strip().split(',')
                theater.add_movie(Movie(title, genre, int(duration)))
        return theater

# Unit Tests
import unittest

class TestTheater(unittest.TestCase):
    def test_import_export_movies(self):
        theater = Theater()
        theater.add_movie(Movie("Inception", "Sci-Fi", 148))
        theater.export_movies_to_txt("Movies.txt")
        imported_theater = Theater.import_movies_from_txt("Movies.txt")
        self.assertEqual(len(imported_theater.movies), 1)
        self.assertEqual(imported_theater.movies[0].title, "Inception")
        self.assertEqual(imported_theater.movies[0].genre, "Sci-Fi")
        self.assertEqual(imported_theater.movies[0].duration, 148)

    def test_singleton(self):
        theater1 = Theater()
        theater2 = Theater()
        self.assertIs(theater1, theater2)

if __name__ == "__main__":
    unittest.main()
