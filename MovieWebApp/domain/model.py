# model.py

# import needed for Review class.
from datetime import datetime


class User:
    def __init__(self, user_name="", password=""):
        if user_name != "" and type(user_name) is str:
            self.user_name = user_name.strip()
        else:
            self.user_name = None
        if password != "" and type(password) is str:
            self.password = password
        else:
            self.password = None
        self.watched_movies = []
        self.reviews = []
        self.time_spent_watching_movies_minutes = int()
        self.watch_list = []

    def __repr__(self):
        return "<User {}>".format(self.user_name)

    def __eq__(self, other):
        return self.user_name == other.user_name

    def __lt__(self, other):
        return str(self.user_name) < str(other.user_name)

    def __hash__(self):
        return hash(self.user_name)

    def add_to_watch_list(self, movie):
        self.watch_list.append(movie)

    def watch_movie(self, movie):
        if movie not in self.watched_movies:
            self.watched_movies.append(movie)
        self.time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review):
        if review not in self.reviews:
            self.reviews.append(review)


class Actor:

    def __init__(self, actor_full_name=""):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name
        self.__colleagues_list = []

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    def __repr__(self):
        return "<Actor {}>".format(self.__actor_full_name)

    def __eq__(self, other):
        return self.__actor_full_name == other.__actor_full_name

    def __lt__(self, other):
        return self.__actor_full_name < other.__actor_full_name

    def __hash__(self):
        return hash(self.__actor_full_name)

    def add_actor_colleague(self, colleague):
        self.__colleagues_list.append(colleague)

    def check_if_this_actor_worked_with(self, colleague):
        return colleague in self.__colleagues_list


class Director:

    def __init__(self, director_full_name=""):
        if director_full_name == "" or type(director_full_name) is not str:
            self._director_full_name = None
        else:
            self._director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self._director_full_name

    def __repr__(self):
        return f"<Director {self._director_full_name}>"

    def __eq__(self, other):
        return self._director_full_name == other.__director_full_name

    def __lt__(self, other):
        return self._director_full_name < other.__director_full_name

    def __hash__(self):
        return hash(self._director_full_name)


class Genre:
    def __init__(self, genre_name=""):
        if genre_name == "" or type(genre_name) is not str:
            self._genre_name = None
        else:
            self._genre_name = genre_name.strip()

    @property
    def genre_name(self) -> str:
        return self._genre_name

    def __repr__(self):
        return "<Genre {}>".format(self._genre_name)

    def __eq__(self, other):
        return self._genre_name == other._genre_name

    def __lt__(self, other):
        return self._genre_name < other._genre_name

    def __hash__(self):
        return hash(self._genre_name)


class Movie:
    def __init__(self, title="", release_year=int()):
        if title != "" and type(title) == str:
            self.title = title.strip()
        if release_year >= 1900:
            self.release_year = release_year
        self.description = ""
        self.director = Director()
        self.actors = []
        self.genres = []
        self.runtime_minutes = int()
        self.rank = int()
        self.rating = float()
        self.revenue = float()

    def add_revenue(self, revenue):
        if revenue == "N/A":
            self.revenue = "N/A"
        else:
            self.revenue = float(revenue)

    def __setattr__(self, key, value):
        self.__dict__[key] = value
        if 'description' in self.__dict__:
            self.__dict__['description'] = self.__dict__['description'].strip()
        if 'runtime_minutes' in self.__dict__:
            if self.__dict__['runtime_minutes'] < 0:
                raise ValueError("Constraint: the runtime is a positive number")

    def __repr__(self):
        return "<Movie {}, {}>".format(self.title, self.release_year)

    def __eq__(self, other):
        string1 = self.title + str(self.release_year)
        string2 = other.title + str(other.release_year)
        return string1 == string2

    def __lt__(self, other):
        string1 = self.title + str(self.release_year)
        string2 = other.title + str(other.release_year)
        return string1 < string2

    def __hash__(self):
        string = self.title + str(self.release_year)
        return hash(string)

    def add_actor(self, actor: Actor):
        self.actors.append(actor)

    def remove_actor(self, actor: Actor):
        if actor in self.actors:
            index = self.actors.index(actor)
            if index != -1:
                self.actors.pop(index)

    def add_genre(self, genre: Genre):
        self.genres.append(genre)

    def remove_genre(self, genre: Genre):
        if genre in self.genres:
            index = self.genres.index(genre)
            if index != -1:
                self.genres.pop(index)


class Review:
    def __init__(self, movie=Movie(), review_text="", rating=float(), timestamp = None):
        if type(rating) == float and rating >= 1 and rating <= 10:
            self.rating = rating
        else:
            self.rating = None
        self.movie = movie
        self.review_text = review_text.strip()
        if timestamp == None:
            now = datetime.now()
            self.timestamp = now.strftime("%c")
        else:
            self.timestamp = timestamp.strftime("%c")

    def __repr__(self):
        return "{}, Review: {}, Rating: {}, Time: {}".format(str(self.movie), str(self.review_text), str(self.rating),
                                                             str(self.timestamp))

    def __eq__(self, other):
        string1 = str(self.movie) + self.review_text + str(self.rating) + str(self.timestamp)
        string2 = str(other.movie) + other.review_text + str(other.rating) + str(other.timestamp)
        return string1 == string2