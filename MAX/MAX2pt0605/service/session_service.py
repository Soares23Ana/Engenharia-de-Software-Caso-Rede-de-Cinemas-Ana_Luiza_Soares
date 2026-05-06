from model.session import Session

class SessionService:
    def __init__(self, repository):
        self.repo = repository

    def registrar_publico(self, session_id, qtd):
        sessao = self.repo.get_by_id(session_id)
        
        if not sessao:
            raise Exception("Erro: Sessão não encontrada!")

        # Regra de Negócio: Validar Capacidade
        if sessao.current_attendance + qtd > sessao.capacity:
            vagas = sessao.capacity - sessao.current_attendance
            raise Exception(f"Erro: Lotação excedida! Restam apenas {vagas} lugares.")

        novo_total = sessao.current_attendance + qtd
        self.repo.update_attendance(session_id, novo_total)
        return f"Sucesso! Novo público da sessão '{sessao.movie_title}': {novo_total}"