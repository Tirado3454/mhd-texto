import streamlit as st
import chess
import chess.svg

# Título da página
st.title("Editor de Tabuleiro de Xadrez")

# Função para exibir o tabuleiro
def exibir_tabuleiro(fen=""):
    board = chess.Board(fen) if fen else chess.Board()
    svg = chess.svg.board(board)
    st.image(svg, use_column_width=True)

# Configuração inicial
if "fen" not in st.session_state:
    st.session_state.fen = ""

# Entrada FEN
st.subheader("Configuração do Tabuleiro")
st.session_state.fen = st.text_input("Insira a FEN do tabuleiro:", st.session_state.fen)

# Botão para atualizar o tabuleiro
if st.button("Atualizar Tabuleiro com FEN"):
    try:
        exibir_tabuleiro(st.session_state.fen)
    except ValueError:
        st.error("FEN inválida. Por favor, insira uma FEN válida.")

# Botão para resetar o tabuleiro
if st.button("Resetar para a posição inicial"):
    st.session_state.fen = ""
    exibir_tabuleiro()

# Exibição do tabuleiro atual
st.subheader("Tabuleiro Atual")
if st.session_state.fen:
    exibir_tabuleiro(st.session_state.fen)
else:
    exibir_tabuleiro()
