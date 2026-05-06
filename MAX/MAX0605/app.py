from repository.movie_repository import MovieRepository
from service.movie_service import MovieService
from controller.movie_controller import MovieController
from view.movie_view import MovieView # Ou MovieViewWeb se estiveres a usar web

def main():
    # 1. Cria a instância do repositório (base de dados)
    repository = MovieRepository()
    
    # 2. Cria o serviço e "injeta" o repositório nele
    service = MovieService(repository)
    
    # 3. Cria o controller e "injeta" o serviço nele
    controller = MovieController(service)
    
    # 4. Cria a view e "injeta" o controller nela
    view = MovieView(controller)
    
    # 5. Inicia a aplicação
    view.exibir_menu() # Ou view.run() se for interface web

if __name__ == "__main__":
    main()