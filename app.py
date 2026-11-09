
import streamlit as st

from main import (
    gerar_regiao_ordenada,
    inserir_chave,
    buscar
)


st.set_page_config(
    page_title="Lista Híbrida",
    page_icon="🔎",
    layout="wide"
)


# INICIALIZAÇÃO DAS LISTAS

if "ordenada" not in st.session_state:
    st.session_state.ordenada = gerar_regiao_ordenada(42)

if "cauda" not in st.session_state:
    st.session_state.cauda = []

if "resultado_busca" not in st.session_state:
    st.session_state.resultado_busca = None


# TÍTULO

st.title("🔎 Lista Híbrida")

st.write(
    "Sistema de busca binária, busca sequencial "
    "e reordenação automática."
)

st.divider()


# INFORMAÇÕES GERAIS

col1, col2, col3 = st.columns(3)

col1.metric(
    "Região ordenada",
    len(st.session_state.ordenada)
)

col2.metric(
    "Elementos na cauda",
    len(st.session_state.cauda)
)

col3.metric(
    "Capacidade da cauda",
    "10"
)


st.divider()


# CAMPO DE ENTRADA

st.subheader("Inserção e busca de chaves")

chave = st.number_input(
    "Digite um número inteiro:",
    step=1,
    value=0
)


col1, col2 = st.columns(2)


# BOTÃO DE INSERÇÃO

with col1:

    if st.button("Inserir chave", use_container_width=True):

        resultado = inserir_chave(
            int(chave),
            st.session_state.ordenada,
            st.session_state.cauda
        )

        st.session_state.resultado_busca = None

        if resultado:
            st.success("Chave inserida com sucesso!")

            if len(st.session_state.cauda) == 0:
                st.info(
                    "A cauda atingiu 10 elementos. "
                    "Reorganização realizada automaticamente!"
                )

        else:
            st.error(
                "Chave repetida! A inserção foi rejeitada."
            )


# BOTÃO DE BUSCA

with col2:

    if st.button("Buscar chave", use_container_width=True):

        st.session_state.resultado_busca = buscar(
            int(chave),
            st.session_state.ordenada,
            st.session_state.cauda
        )


# RESULTADO DA BUSCA

resultado = st.session_state.resultado_busca

if resultado is not None:

    st.divider()

    st.subheader("Resultado da busca")

    if resultado["local"] != "Não encontrada":
        st.success(
            f"Chave encontrada em: {resultado['local']}"
        )
    else:
        st.error("Chave não encontrada nas listas.")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Iterações binárias",
        resultado["iteracoes_binarias"]
    )

    col2.metric(
        "Iterações sequenciais",
        resultado["iteracoes_sequenciais"]
    )

    col3.metric(
        "Total de iterações",
        resultado["total"]
    )

    if resultado["posicao"] != -1:
        st.info(
            f"Posição na região encontrada: "
            f"{resultado['posicao']}"
        )


st.divider()


# EXIBIÇÃO DAS LISTAS

st.subheader("Estrutura de armazenamento")

col1, col2 = st.columns(2)

with col1:

    st.markdown("### Região ordenada")

    st.dataframe(
        [
            {"Índice": i, "Chave": numero}
            for i, numero in enumerate(
                st.session_state.ordenada
            )
        ],
        use_container_width=True,
        height=400
    )

with col2:

    st.markdown("### Cauda não ordenada")

    if st.session_state.cauda:

        st.dataframe(
            [
                {"Índice": i, "Chave": numero}
                for i, numero in enumerate(
                    st.session_state.cauda
                )
            ],
            use_container_width=True,
            height=400
        )

    else:
        st.info("A cauda está vazia.")


st.divider()


# BOTÃO DE REINICIALIZAÇÃO

if st.button("Reiniciar aplicação"):

    st.session_state.ordenada = gerar_regiao_ordenada(42)
    st.session_state.cauda = []
    st.session_state.resultado_busca = None

    st.rerun()


# INFORMAÇÕES DOS COMPONENTES

with st.expander("Componentes Streamlit utilizados"):

    st.write("""
    - st.set_page_config()
    - st.title()
    - st.write()
    - st.divider()
    - st.columns()
    - st.metric()
    - st.number_input()
    - st.button()
    - st.success()
    - st.error()
    - st.info()
    - st.subheader()
    - st.markdown()
    - st.dataframe()
    - st.expander()
    - st.rerun()
    - st.session_state
    """)
