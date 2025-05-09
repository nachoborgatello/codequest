import pytest
from src.core.game import CodeQuestGame

@pytest.fixture
def game():
    return CodeQuestGame("data/questions.json")

def test_load_questions(game):
    assert len(game.questions) > 0, "Debe haber preguntas cargadas"

def test_correct_answer(game):
    game.ask_question(0)  # Simula pregunta (mockear input en pruebas reales)
    assert game.current_score == 10, "Puntuación debe aumentar con respuesta correcta"