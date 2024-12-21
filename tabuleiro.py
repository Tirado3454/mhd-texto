import streamlit as st
import chess
import chess.svg

def main():
    st.title("Editor de Tabuleiro de Xadrez")

    # Inicializar o tabuleiro no estado inicial, se não estiver configurado
    if "tabuleiro" not in st.session_state:
        st.session_state.tabuleiro = chess.Board()

    tabuleiro = st.session_state.tabuleiro

    # Renderizar o tabuleiro usando chess.svg
    st.subheader("Tabuleiro Atual")
    tabuleiro_svg = chess.svg.board(tabuleiro)
    st.write(f"<div style='text-align: center;'>{tabuleiro_svg}</div>", unsafe_allow_html=True)

    # Controles para modificar o tabuleiro
    st.subheader("Editar Tabuleiro")
    movimento = st.text_input("Digite o movimento (ex: 'e2e4'):")

    if st.button("Mover"):
        try:
            tabuleiro.push_san(movimento)
            st.success(f"Movimento '{movimento}' realizado.")
        except ValueError:
            st.error("Movimento inválido. Tente novamente.")

    # Botão para resetar o tabuleiro
    if st.button("Resetar Tabuleiro"):
        st.session_state.tabuleiro = chess.Board()
        st.success("Tabuleiro resetado para o estado inicial.")

if __name__ == "__main__":
    main()
