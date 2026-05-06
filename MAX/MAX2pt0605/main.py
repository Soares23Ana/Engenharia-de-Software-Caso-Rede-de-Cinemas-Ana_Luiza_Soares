from repository.session_repository import SessionRepository
from service.session_service import SessionService
from controller.movie_controller import MovieController
from view.movie_view import MovieView

def main():
    # Injeção das sessões
    session_repo = SessionRepository()
    session_service = SessionService(session_repo)
    
    # Criamos o controller (passamos None para o movie_service por agora)
    controller = MovieController(None, session_service)
    
    view = MovieView(controller)
    view.exibir_menu()

if __name__ == "__main__":
    main()