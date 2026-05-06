class MovieController:
    def __init__(self, movie_service, session_service):
        self.movie_service = movie_service
        self.session_service = session_service

    def add_attendance(self, session_id, qtd):
        try:
            return self.session_service.registrar_publico(session_id, qtd)
        except Exception as e:
            return str(e)