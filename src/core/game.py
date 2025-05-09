class CodeQuestGame:
    def __init__(self, question_manager):
        self.question_manager = question_manager
        self.current_score = 0

    def reset_game(self):
        self.current_score = 0