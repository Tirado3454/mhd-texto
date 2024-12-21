import streamlit as st

# Inicializar o estado
if "etapas" not in st.session_state:
    st.session_state.etapas = []
if "descricao_etapa" not in st.session_state:
    st.session_state.descricao_etapa = ""

# Função para adicionar etapa
def adicionar_etapa():
    if st.session_state.descricao_etapa:
        st.session_state.etapas.append(
            {
                "topico": st.session_state.topico_selecionado,
                "descricao": st.session_state.descricao_etapa,
            }
        )
        st.session_state.descricao_etapa = ""  # Limpar o campo de descrição

# Títulos e introdução
st.title("Interface MHD - Etapas Escritas")
st.header("Etapas do Modelo Hipotético-Dedutivo")

# Seção de seleção de tópicos
st.subheader("Tópicos do MHD")
topicos_mhd = ["Observação", "Hipótese", "Experimento", "Teoria"]
st.session_state.topico_selecionado = st.selectbox(
    "Selecione um tópico do MHD:", topicos_mhd
)

# Exibir dica com base no tópico selecionado
dicas = {
    "Observação": "Observe atentamente e registre os detalhes relevantes.",
    "Hipótese": "Levante hipóteses sobre possíveis padrões ou explicações.",
    "Experimento": "Teste suas hipóteses de maneira controlada.",
    "Teoria": "Elabore uma teoria baseada nas observações e experimentos.",
}
st.info(dicas[st.session_state.topico_selecionado])

# Campo para descrição da etapa
st.subheader("Descreva a etapa")
st.session_state.descricao_etapa = st.text_area(
    "Descrição da etapa:", value=st.session_state.descricao_etapa
)

# Botão para adicionar etapa
if st.button("Adicionar etapa"):
    adicionar_etapa()

# Listar as etapas adicionadas
st.subheader("Etapas Adicionadas")
if st.session_state.etapas:
    for idx, etapa in enumerate(st.session_state.etapas):
        st.write(f"**Etapa {idx + 1}: {etapa['topico']}**")
        st.write(etapa["descricao"])
else:
    st.info("Nenhuma etapa adicionada ainda.")
