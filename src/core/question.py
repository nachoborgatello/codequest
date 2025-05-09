import json
from pathlib import Path
from typing import List, Dict

class Question:
    def __init__(self, text: str, options: List[str], correct: int, category: str = "general"):
        self.text = text
        self.options = options
        self.correct = correct  # Índice de la opción correcta
        self.category = category

    def validate(self) -> bool:
        """Valida que la pregunta sea correcta."""
        return (
            len(self.options) >= 2 and
            0 <= self.correct < len(self.options) and
            isinstance(self.text, str) and
            len(self.text) > 0
        )

class QuestionManager:
    def __init__(self, questions_file: str = "data/questions.json"):
        self.questions_file = Path(questions_file)
        self.questions: List[Question] = []
        self.load_questions()
        if not self.questions:  # ← Nueva validación
            raise ValueError("No se cargaron preguntas. Verifica el archivo JSON.")

    def load_questions(self) -> None:
        """Carga preguntas desde un archivo JSON y las valida."""
        if not self.questions_file.exists():
            raise FileNotFoundError(f"Archivo {self.questions_file} no encontrado")

        with open(self.questions_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        for idx, q in enumerate(data):
            question = Question(
                text=q["text"],
                options=q["options"],
                correct=q["correct"],
                category=q.get("category", "general")
            )
            if not question.validate():
                raise ValueError(f"Pregunta inválida en posición {idx}: {q}")
            self.questions.append(question)

    def get_by_category(self, category: str) -> List[Question]:
        """Filtra preguntas por categoría."""
        return [q for q in self.questions if q.category == category]