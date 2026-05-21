import streamlit as st
import pandas as pd

# CONFIGURAÇÃO DEVE SER A PRIMEIRA COISA
st.set_page_config(page_title="Gestão de Turmas", layout="wide")

# --- DADOS MOCKADOS (ESTRUTURA IGUAL À API) ---
data = {
    "metricas": {
        "alunos_base": "93",
        "prontos_aula": "10",
        "assunto_critico": "Teorema de Pitágoras"
    },
    "turmas": [
        {"id": "3A", "nome": "3º Ano A - Matutino", "alunos": 35, "status": "Crítico", "nivelamento": 45},
        {"id": "3B", "nome": "3º Ano B - Matutino", "alunos": 30, "status": "Estável", "nivelamento": 72},
        {"id": "2C", "nome": "2º Ano C - Vespertino", "alunos": 28, "status": "Excelente", "nivelamento": 91}
    ]
}

def status_indicator(cor_hex):
    return f"""
    <span style="
        height: 20px;
        width: 20px;
        background-color: {cor_hex};
        border-radius: 50%;
        display: inline-block;
        margin-right: 8px;
        vertical-align: middle;
    "></span>
    """

cores_map = {
    "Crítico": "#FF4B4B",
    "Estável": "#FFA500",
    "Excelente": "#2ECC71"
}

def dashboard_professor():
    st.title("Painel do Professor")
    
    # --- 1. MÉTRICAS ---
    metricas = data['metricas']
    col_m1, col_m2, col_m3 = st.columns(3)
    col_m1.metric("Alunos na Base", metricas['alunos_base'], border=True)
    col_m2.metric("Prontos para Aula", metricas['prontos_aula'], border=True)
    col_m3.metric("Assunto Crítico", metricas['assunto_critico'], border=True)

    # --- 2. BOTÕES DE INSERÇÃO (POPOVERS) ---
    st.write("") 
    col_btn1, col_btn2, _ = st.columns([1, 1, 2])

    with col_btn1:
        with st.popover("Inserir Novo Assunto", use_container_width=True):
            st.markdown("### Novo Assunto")
            nome_assunto = st.text_input("Nome do Tópico", placeholder="Ex: Logaritmos")
            desc_assunto = st.text_area("Descrição")
            pre_reqs = st.multiselect("Pré-requisitos", ["Potenciação", "Equação", "Frações"])
            if st.button("Cadastrar Assunto", type="primary"):
                st.success(f"Assunto '{nome_assunto}' adicionado!")

    with col_btn2:
        with st.popover("Inserir Novo Aluno", use_container_width=True):
            st.markdown("### Novo Aluno")
            nome_aluno = st.text_input("Nome Completo")
            # Usa os dados do mock para preencher o selectbox
            turma_aluno = st.selectbox("Vincular à Turma", [t["nome"] for t in data['turmas']])
            if st.button("Cadastrar Aluno", type="primary"):
                st.success(f"Aluno '{nome_aluno}' cadastrado!")

    st.markdown("---")
    
    # --- 3. LISTA DE TURMAS ---
    st.subheader("Lista de Turmas")

    col_h1, col_h2, col_h3, col_h4 = st.columns([3, 1, 2, 1])
    with col_h1: st.markdown("**Nome da Turma**")
    with col_h2: st.markdown("**Qtd. Alunos**")
    with col_h3: st.markdown("**Nivelamento**")
    with col_h4: st.markdown("**Ação**")
    
    st.divider()

    for turma in data['turmas']:
        with st.container():
            c1, c2, c3, c4 = st.columns([3, 1, 2, 1])
            with c1:
                cor_atual = cores_map.get(turma['status'], "#777")
                st.markdown(f"{status_indicator(cor_atual)} {turma['nome']}", unsafe_allow_html=True)
                st.caption(f"Status: {turma['status']}")
            with c2:
                st.write(f"{turma['alunos']}")
            with c3:
                st.write("") 
                st.progress(turma['nivelamento'] / 100)
            with c4:
                # Importante: O arquivo precisa existir na pasta pages/ para funcionar
                st.page_link("pages/turma.py", label="Ver Detalhes", icon="📊", use_container_width=True)
            st.markdown("---")

if __name__ == "__main__":
    dashboard_professor()