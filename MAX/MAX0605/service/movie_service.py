class MovieService:
    def __init__(self, repository):
        self.repo = repository

    def register_movie(self, title, duration, director):
        if duration <= 0:
            raise ValueError("Duração deve ser positiva.")
        new_movie = Movie(None, title, duration, director)
        self.repo.save(new_movie)