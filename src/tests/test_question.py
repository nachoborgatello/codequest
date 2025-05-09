import pytest
from src.core.question import Question, QuestionManager
import tempfile
import json

# Fixture para datos de prueba
@pytest.fixture
def sample_questions_file():
    data = [
        {
            "text": "¿Qué es Python?",
            "options": ["Un lenguaje de programación", "Una serpiente", "Un framework"],
            "correct": 0,
            "category": "python"
        }
    ]
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump(data, f)
        f.flush()
        yield f.name  # Ruta del archivo temporal

# Tests para la clase Question
def test_question_validation():
    valid_question = Question("Test", ["A", "B"], 0)
    assert valid_question.validate()

    invalid_question = Question("", ["A"], 1)  # Texto vacío
    assert not invalid_question.validate()

# Tests para QuestionManager
def test_load_questions(sample_questions_file):
    manager = QuestionManager(sample_questions_file)
    assert len(manager.questions) == 1
    assert manager.questions[0].text == "¿Qué es Python?"

def test_get_by_category(sample_questions_file):
    manager = QuestionManager(sample_questions_file)
    python_questions = manager.get_by_category("python")
    assert len(python_questions) == 1
    assert manager.get_by_category("inexistente") == []