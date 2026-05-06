# main.py
from view.movie_view import MovieView
from controller.movie_controller import MovieController
from service.movie_service import MovieService
from repository.movie_repository import MovieRepository

def bootstrap():
    
    repository = MovieRepository()
    
   
    
  
    controller = MovieController(service)
    
    
    app = MovieView(controller)
    
    
    app.exibir_menu()

if __name__ == "__main__":
    bootstrap()