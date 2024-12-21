import streamlit as st
import chess
import chess.svg

# T�tulo da p�gina
st.title("Editor de Tabuleiro de Xadrez")

# Fun��o para exibir o tabuleiro
def exibir_tabuleiro(fen=""):
    board = chess.Board(fen) if fen else chess.Board()
    svg = chess.svg.board(board)
    st.image(svg, use_column_width=True)

# Configura��o inicial
if "fen" not in st.session_state:
    st.session_state.fen = ""

# Entrada FEN
st.subheader("Configura��o do Tabuleiro")
st.session_state.fen = st.text_input("Insira a FEN do tabuleiro:", st.session_state.fen)

# Bot�o para atualizar o tabuleiro
if st.button("Atualizar Tabuleiro com FEN"):
    try:
        exibir_tabuleiro(st.session_state.fen)
    except ValueError:
        st.error("FEN inv�lida. Por favor, insira uma FEN v�lida.")

# Bot�o para resetar o tabuleiro
if st.button("Resetar para a posi��o inicial"):
    st.session_state.fen = ""
    exibir_tabuleiro()

# Exibi��o do tabuleiro atual
st.subheader("Tabuleiro Atual")
if st.session_state.fen:
    exibir_tabuleiro(st.session_state.fen)
else:
    exibir_tabuleiro()
