class MovieView:
    def __init__(self, controller):
        self.controller = controller

    def exibir_menu(self):
        while True:
            print("\n--- SISTEMA DE GESTÃO DE CINEMA ---")
            print("1. Cadastrar Novo Filme")
            print("0. Sair")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                self.solicitar_cadastro_filme()
            elif opcao == "0":
                print("A encerrar sistema...")
                break
            else:
                print("Opção inválida.")

    def solicitar_cadastro_filme(self):
        print("\n--- CADASTRO DE FILME ---")
        titulo = input("Título do Filme: ")
        try:
            duracao = int(input("Duração (em minutos): "))
            diretor = input("Nome do Diretor: ")
            
            # Chama o Controller
            resultado = self.controller.add_movie(titulo, duracao, diretor)
            print(resultado)
        except ValueError:
            print("Erro: A duração deve ser um número inteiro.")

# --- PONTO DE ENTRADA (MAIN) ---
if __name__ == "__main__":
    from movie_repository import MovieRepository
    from movie_service import MovieService
    from movie_controller import MovieController

    # Injeção de Dependências
    repo = MovieRepository()
    service = MovieService(repo)
    controller = MovieController(service)
    
    # Inicia a Interface
    view = MovieView(controller)
    view.exibir_menu()