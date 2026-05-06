class MovieView:
    def __init__(self, controller):
        self.controller = controller

    def exibir_menu(self):
        while True:
            print("\n--- GESTÃO DE SESSÕES (CINEMA) ---")
            print("1. Registrar Público em Sessão")
            print("0. Sair")
            op = input("Escolha: ")
            
            if op == "1":
                sid = int(input("ID da Sessão (tenta 1 ou 2): "))
                qtd = int(input("Quantidade de pessoas a entrar: "))
                print(self.controller.add_attendance(sid, qtd))
            elif op == "0":
                break