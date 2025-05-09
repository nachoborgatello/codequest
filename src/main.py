import argparse
from src.core.game import CodeQuestGame
from src.core.question import QuestionManager
from src.interface.cli import start_cli_game
from src.interface.web import start_web_game

def main():
    parser = argparse.ArgumentParser(description="🌟 CodeAdventure - Juego de Preguntas de Programación")
    parser.add_argument(
        "--mode",
        choices=["cli", "web"],
        default="cli",
        help="Modo de ejecución (consola o web)"
    )
    args = parser.parse_args()

    # Cargar preguntas y inicializar juego
    question_manager = QuestionManager("data/questions.json")
    game = CodeQuestGame(question_manager)

    if args.mode == "cli":
        start_cli_game(game)
    else:
        start_web_game(game)

if __name__ == "__main__":
    main()