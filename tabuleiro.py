import streamlit as st
import chess
import chess.svg
from cairosvg import svg2png

# Função para renderizar o tabuleiro
def renderizar_tabuleiro(tabuleiro):
    svg = chess.svg.board(tabuleiro)
    png = svg2png(bytestring=svg)
    return png

def main():
    st.title("Editor de Tabuleiro de Xadrez")

    # Inicializar o tabuleiro
    if "tabuleiro" not in st.session_state:
        st.session_state.tabuleiro = chess.Board()

    tabuleiro = st.session_state.tabuleiro

    # Renderizar o tabuleiro
    st.image(renderizar_tabuleiro(tabuleiro), caption="Tabuleiro Atual", use_column_width=True)

    # Controles para adicionar ou remover peças
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
