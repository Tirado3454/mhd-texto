import streamlit as st

# Inicializar o tabuleiro como uma matriz 8x8
def inicializar_tabuleiro():
    return [["" for _ in range(8)] for _ in range(8)]

# Renderizar o tabuleiro no Streamlit
def renderizar_tabuleiro(tabuleiro):
    st.write("Tabuleiro de Xadrez")
    for linha in tabuleiro:
        st.write(" | ".join(celula if celula else "." for celula in linha))

# Atualizar uma posição no tabuleiro
def atualizar_tabuleiro(tabuleiro, posicao, peca):
    try:
        coluna, linha = posicao[0].lower(), int(posicao[1])
        col_idx = ord(coluna) - ord('a')
        row_idx = 8 - linha
        if 0 <= col_idx < 8 and 0 <= row_idx < 8:
            tabuleiro[row_idx][col_idx] = peca
            return True
        else:
            return False
    except (IndexError, ValueError):
        return False

# Remover uma peça do tabuleiro
def remover_peca(tabuleiro, posicao):
    atualizar_tabuleiro(tabuleiro, posicao, "")

# Interface principal
def main():
    st.title("Editor de Tabuleiro de Xadrez")
    if "tabuleiro" not in st.session_state:
        st.session_state.tabuleiro = inicializar_tabuleiro()

    tabuleiro = st.session_state.tabuleiro

    # Renderizar o tabuleiro
    renderizar_tabuleiro(tabuleiro)

    # Controles para adicionar peças
    st.subheader("Adicionar peça")
    peca = st.text_input("Digite a peça (ex: 'P', 'T', 'C', etc.):")
    posicao = st.text_input("Digite a posição (ex: 'e2'):")

    if st.button("Adicionar"):
        if atualizar_tabuleiro(tabuleiro, posicao, peca):
            st.success(f"Peça '{peca}' adicionada na posição {posicao}.")
        else:
            st.error("Posição inválida.")

    # Controles para remover peças
    st.subheader("Remover peça")
    posicao_remover = st.text_input("Digite a posição para remover (ex: 'e2'):")

    if st.button("Remover"):
        if atualizar_tabuleiro(tabuleiro, posicao_remover, ""):
            st.success(f"Peça removida da posição {posicao_remover}.")
        else:
            st.error("Posição inválida.")

    # Botão para resetar o tabuleiro
    if st.button("Resetar tabuleiro"):
        st.session_state.tabuleiro = inicializar_tabuleiro()
        st.success("Tabuleiro resetado.")

if __name__ == "__main__":
    main()
