import streamlit as st
from src.core.game import CodeQuestGame

def start_web_game(game):
    st.set_page_config(page_title="CodeAdventure", page_icon="❓")
    st.title("🎮 CodeAdventure (Web)")

    if not game.question_manager.questions:  # ← Nueva validación
        st.error("⚠️ No hay preguntas disponibles. Carga algunas en data/questions.json")
        return

    if "current_question" not in st.session_state:
        st.session_state.current_question = 0
        st.session_state.score = 0

    # Verifica que el índice sea válido
    if st.session_state.current_question >= len(game.question_manager.questions):
        st.balloons()
        st.success(f"✨ ¡Juego completado! Puntuación: {st.session_state.score}")
        return

    question = game.question_manager.questions[st.session_state.current_question]

    with st.form("question_form"):
        st.subheader(f"Pregunta {st.session_state.current_question + 1}")
        st.markdown(f"**{question.text}**")
        
        user_answer = st.radio("Opciones:", question.options, index=None)
        submitted = st.form_submit_button("Enviar")

        if submitted and user_answer:
            if user_answer == question.options[question.correct]:
                st.session_state.score += 10
                st.success("✅ ¡Correcto! +10 puntos")
            else:
                st.error(f"❌ Incorrecto. La respuesta correcta era: **{question.options[question.correct]}**")

            st.session_state.current_question += 1
            if st.session_state.current_question >= len(game.question_manager.questions):
                st.balloons()
                st.success(f"✨ ¡Juego completado! Puntuación: {st.session_state.score}/{len(game.question_manager.questions) * 10}")
            else:
                st.experimental_rerun()