from model.session import Session

class SessionRepository:
    def __init__(self):
        # Criamos uma sessão de teste para poderes usar no terminal
        self.sessions = {
            1: Session(1, "Batman", 100, 80),
            2: Session(2, "Avatar", 50, 45)
        }

    def get_by_id(self, session_id):
        return self.sessions.get(session_id)

    def update_attendance(self, session_id, new_total):
        if session_id in self.sessions:
            self.sessions[session_id].current_attendance = new_total
            return True
        return False