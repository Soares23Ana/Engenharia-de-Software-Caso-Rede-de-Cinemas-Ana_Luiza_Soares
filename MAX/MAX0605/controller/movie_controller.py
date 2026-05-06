class MovieController:
    def __init__(self, service):
        self.service = service

    def add_movie(self, title, duration, director):
        try:
            self.service.register_movie(title, duration, director)
            return "Filme cadastrado com sucesso!"
        except Exception as e:
            return f"Erro: {str(e)}"