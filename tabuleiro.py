import streamlit as st

def text_section():
    # Inicialização do estado da sessão
    if 'etapas' not in st.session_state:
        st.session_state['etapas'] = []
    if 'descricao_etapa' not in st.session_state:
        st.session_state['descricao_etapa'] = ""

    # Função para obter a dica com base no tópico selecionado
    def obter_dica(topico):
        dicas = {
            "Teórica": "Explique a fundamentação teórica relacionada ao problema.",
            "Hipótese": "Formule a hipótese com base na análise teórica.",
            "Planejamento": "Descreva como o problema será resolvido.",
            "Execução": "Mostre os resultados da implementação.",
            "Avaliação": "Analise os resultados obtidos em relação ao esperado.",
        }
        return dicas.get(topico, "Selecione um tópico para visualizar a dica.")

    # Layout para os tópicos do MHD
    st.subheader("Selecione o tópico da etapa:")
    topico = st.selectbox("", ["Selecione", "Teórica", "Hipótese", "Planejamento", "Execução", "Avaliação"])

    # Exibe a dica correspondente
    if topico != "Selecione":
        st.info(obter_dica(topico))

    # Campo de descrição para adicionar etapas
    st.subheader("Descreva a etapa:")
    descricao = st.text_area("", key="descricao_etapa")

    # Botão para adicionar nova etapa
    if st.button("Adicionar Etapa"):
        if descricao:
            st.session_state['etapas'].append({"topico": topico, "descricao": descricao})
            st.session_state['descricao_etapa'] = ""  # Limpa o campo de descrição
            st.success("Etapa adicionada com sucesso!")
        else:
            st.warning("Por favor, insira uma descrição para a etapa.")

    # Exibe as etapas adicionadas
    st.subheader("Etapas Adicionadas:")
    if st.session_state['etapas']:
        for i, etapa in enumerate(st.session_state['etapas'], 1):
            st.write(f"**Etapa {i}:** {etapa['topico']} - {etapa['descricao']}")
    else:
        st.write("Nenhuma etapa adicionada até agora.")
