def start_cli_game(game):
    print("🎮 ¡Bienvenido a CodeAdventure (Modo Consola)!")
    print(f"Hay {len(game.question_manager.questions)} preguntas disponibles.\n")

    for question in game.question_manager.questions:
        print(f"📌 {question.text}")
        for idx, option in enumerate(question.options):
            print(f"  {idx + 1}. {option}")

        user_answer = int(input("\nTu respuesta (número): ")) - 1
        if user_answer == question.correct:
            game.current_score += 10
            print("✅ ¡Correcto! +10 puntos\n")
        else:
            print(f"❌ Incorrecto. La respuesta era: {question.correct + 1}\n")

    print(f"🎉 Puntuación final: {game.current_score}/{(len(game.question_manager.questions) * 10)}")