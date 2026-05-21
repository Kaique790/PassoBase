import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Perfil do Aluno", layout="wide")

# Link para voltar à página da turma
st.page_link("pages/Turma.py", label="<- Voltar para a Turma")

st.title("Perfil Individual do Aluno")
st.divider()

# --- DADOS MOCKADOS POR TÓPICO ---
dados_topicos = {
    "Potenciação": [30, 45, 40, 55, 62],
    "Equação 1º Grau": [50, 60, 75, 80, 85],
    "Frações": [20, 25, 30, 28, 40],
    "Pitágoras": [70, 72, 80, 88, 92]
}
datas = ["01/10", "05/10", "10/10", "15/10", "20/10"]

col1, col2 = st.columns([1, 2])

with col1:
    st.info("### Lucas Aluno")
    
    # --- MÉTRICA DE DESTAQUE ---
    # Calcula a média ou tendência para mostrar algo relevante
    st.metric(label="Proficiência Geral", value="74%", delta="12% (Últimos 30 dias)", border=True)
    
    st.write("**Série:** 3º Ano A")
    st.write("**Engajamento:** Alto")
    st.write("**Última atividade:** Ontem")
    
    st.divider()
    
    # --- SELETOR DE TÓPICO ---
    topico_selecionado = st.selectbox(
        "Selecione o tópico para análise:",
        options=list(dados_topicos.keys())
    )

with col2:
    st.subheader(f"Evolução em: {topico_selecionado}")
    
    # Criando o DataFrame baseado na seleção
    df_evolucao = pd.DataFrame({
        "Data": datas,
        "Nota": dados_topicos[topico_selecionado]
    })
    
    # Gerando o gráfico dinâmico
    fig = px.line(
        df_evolucao, 
        x="Data", 
        y="Nota", 
        markers=True,
        range_y=[0, 100], # Mantém a escala fixa para facilitar a comparação
        color_discrete_sequence=["#7D3CFF"] # Cor roxa para combinar com o estilo anterior
    )
    
    # Estilização do gráfico
    fig.update_layout(xaxis_title="Período", yaxis_title="Nível de Proficiência (%)")
    
    st.plotly_chart(fig, use_container_width=True)

# --- MÉTRICA EXTRA ABAIXO DO GRÁFICO ---
c1, c2, c3 = st.columns(3)
with c1:
    nota_atual = dados_topicos[topico_selecionado][-1]
    st.metric("Nível Atual", f"{nota_atual}%", border=True)
with c2:
    status = "Acima da Média" if nota_atual > 60 else "Abaixo da Média"
    st.metric("Status no Tópico", status, border=True)
with c3:
    st.metric("Tempo de Estudo", "4.5h", border=True)
