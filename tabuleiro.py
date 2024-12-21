import streamlit as st
import chess
import chess.svg
from cairosvg import svg2png

def render_chessboard(board):
    """Renderiza o tabuleiro de xadrez em formato PNG para exibição no Streamlit."""
    svg = chess.svg.board(board=board)
    png = svg2png(bytestring=svg)
    return png

def main():
    st.title("Editor de Tabuleiro de Xadrez")

    # Inicializando o tabuleiro
    if "chessboard" not in st.session_state:
        st.session_state.chessboard = chess.Board()

    board = st.session_state.chessboard

    # Renderiza o tabuleiro
    st.image(render_chessboard(board), use_column_width=True)

    # Controle para escolher a ação
    col1, col2 = st.columns(2)

    with col1:
        st.write("Escolha uma peça para adicionar:")
        piece = st.selectbox("Peça", ["Peão", "Cavalo", "Bispo", "Torre", "Rainha", "Rei"])
        color = st.radio("Cor", ["Branca", "Preta"])
        position = st.text_input("Posição no tabuleiro (ex: e2):")

    with col2:
        st.write("Remova uma peça:")
        remove_position = st.text_input("Posição para remover (ex: e2):")

    # Adicionar peça ao tabuleiro
    if st.button("Adicionar peça"):
        if position:
            try:
                square = chess.parse_square(position)
                piece_map = {
                    "Peão": chess.PAWN,
                    "Cavalo": chess.KNIGHT,
                    "Bispo": chess.BISHOP,
                    "Torre": chess.ROOK,
                    "Rainha": chess.QUEEN,
                    "Rei": chess.KING,
                }
                piece_color = chess.WHITE if color == "Branca" else chess.BLACK
                board.set_piece_at(square, chess.Piece(piece_map[piece], piece_color))
                st.success(f"{piece} {color} adicionado na posição {position}.")
            except ValueError:
                st.error("Posição inválida.")

    # Remover peça do tabuleiro
    if st.button("Remover peça"):
        if remove_position:
            try:
                square = chess.parse_square(remove_position)
                board.remove_piece_at(square)
                st.success(f"Peça removida da posição {remove_position}.")
            except ValueError:
                st.error("Posição inválida.")

    # Botão para resetar o tabuleiro
    if st.button("Resetar tabuleiro"):
        board.reset()
        st.success("Tabuleiro resetado para a posição inicial.")

if __name__ == "__main__":
    main()
