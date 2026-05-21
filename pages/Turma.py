import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="Detalhes da Turma", layout="wide")

# Estilo para os Badges de Situação
def render_badge(texto, cor_fundo):
    return f"""
        <span style="
            background-color: {cor_fundo};
            color: white;
            padding: 2px 10px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: bold;
            display: inline-block;
        ">
            {texto.upper()}
        </span>
    """

# Botão para voltar ao iníciost.page_link("Início.py", label="<- Voltar para Minhas Turmas")


st.title("Detalhes da Turma")
st.divider()

# --- 1. GRÁFICO DE DESEMPENHO ---
st.subheader("Desempenho por Tópico")
df_grafico = pd.DataFrame({
    "Tópico": ["Frações", "Potenciação", "Equação", "Geometria"],
    "Proficiência": [85, 42, 60, 75]
})

fig = px.bar(df_grafico, x="Tópico", y="Proficiência", 
             color="Proficiência", color_continuous_scale="RdYlGn",
             range_y=[0, 100])
st.plotly_chart(fig, use_container_width=True)

st.divider()
# --- NOVO: SEÇÃO DE DIAGNÓSTICO GERAL (POPOVER) ---
col_diag, _ = st.columns([1, 3])
with col_diag:
    with st.popover("Gerar Diagnóstico Geral", use_container_width=True):
        st.markdown("### Diagnóstico Geral")
        st.write("Avaliação de pré-requisitos para identificação de lacunas semestrais:")
        
        # Lista simples de perguntas/testes
        st.markdown("""
        1. **Teste de divisão** (Operações fundamentais)
        2. **Teste de MMC** (Mínimo Múltiplo Comum)
        3. **Teste de soma e subtração de frações**
        4. **Teste de interpretação de problemas**
        5. **Teste de raciocínio lógico básico**
        """)
        
        st.divider()
        if st.button("Aplicar para esta turma", type="primary"):
            st.success("Diagnóstico agendado para a próxima aula!")

st.divider()

# --- 2. LISTA DE ALUNOS ---
st.subheader("Lista de Alunos")

# Dados Mockados dos Alunos
MOCK_ALUNOS = [
    {"nome": "Lucas Aluno", "situacao": "Pronto", "cor": "#2ecc71"},
    {"nome": "Juliana Aluna", "situacao": "Em Alerta", "cor": "#ff4b4b"},
    {"nome": "Pedro Aluno", "situacao": "Em Andamento", "cor": "#f39c12"},
    {"nome": "Mariana Souza", "situacao": "Pronto", "cor": "#2ecc71"},
]

# Cabeçalho da Lista
col_h1, col_h2, col_h3 = st.columns([3, 2, 1])
with col_h1: st.markdown("**Nome do Aluno**")
with col_h2: st.markdown("**Situação**")
with col_h3: st.markdown("**Ação**")

st.divider()

# Renderização dos Alunos
for aluno in MOCK_ALUNOS:
    c1, c2, c3 = st.columns([3, 2, 1])
    
    with c1:
        st.write(f"**{aluno['nome']}**")
    
    with c2:
        st.markdown(render_badge(aluno['situacao'], aluno['cor']), unsafe_allow_html=True)
    
    with c3:
        with st.container(border=True):
            st.page_link("pages/aluno.py", label="ACESSAR", use_container_width=True)
    
    st.markdown("<div style='margin-bottom: -15px;'></div>", unsafe_allow_html=True)
    st.divider()