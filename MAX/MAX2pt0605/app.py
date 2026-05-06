# Importação das camadas para Cinema
from repository.session_repository import SessionRepository
from service.session_service import SessionService
from controller.session_controller import MovieController
from view.movie_view import MovieView

def main():
    # 1. REPOSITORY: Responsável pelo acesso ao banco de dados
    session_repo = SessionRepository()
    
    # 2. SERVICE: Responsável pelas Regras de Negócio
    session_service = SessionService(session_repo)
    
    # 3. CONTROLLER: O orquestrador
    # Passamos None para movie_service porque o código atual só usa session_service
    controller = MovieController(None, session_service)
    
    # 4. VIEW: A interface com o utilizador
    view = MovieView(controller)
    
    # 5. EXECUÇÃO
    view.exibir_menu()

if __name__ == "__main__":
    main()