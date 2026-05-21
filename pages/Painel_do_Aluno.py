import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página para o Aluno
st.set_page_config(page_title="Minha Jornada de Aprendizado", layout="wide")

# --- ESTILIZAÇÃO MINIMALISTA ---
def status_dot(color):
    return f"""
    <span style="
        height: 12px;
        width: 12px;
        background-color: {color};
        border-radius: 50%;
        display: inline-block;
        margin-right: 8px;
    "></span>
    """

def card_aluno():
    st.title("Minha Jornada")
    
    # --- 1. RESUMO DE CONQUISTAS (Métricas do Aluno) ---
    col_m1, col_m2, col_m3 = st.columns(3)
    col_m1.metric("Meu Nivelamento Médio", "74%", delta="5% esta semana", border=True)
    col_m2.metric("Assuntos Concluídos", "12", help="Tópicos onde você atingiu 100%", border=True)
    col_m3.metric("Próximo Desafio", "Logaritmos", help="Assunto que será liberado em breve", border=True)

    st.write("") 

    # --- 2. ÁREA DE FOCO (O que fazer agora?) ---
    with st.expander("🎯 Onde devo focar hoje?", expanded=True):
        col_f1, col_f2 = st.columns([2, 1])
        with col_f1:
            st.warning("**Atenção em: Potenciação**")
            st.write("Seu desempenho caiu um pouco aqui. Que tal revisar as propriedades de potências de mesma base?")
        with col_f2:
            if st.button("Abrir Revisão", use_container_width=True, type="primary"):
                st.balloons() # Feedback de gamificação

    st.markdown("---")

    # --- 3. MEU PROGRESSO DETALHADO ---
    st.subheader("Meus Conhecimentos")
    
    # Dados de exemplo do aluno
    meus_assuntos = {
        "Frações": {"progresso": 100, "status": "Excelente", "cor": "#2ECC71"},
        "Equação 1º Grau": {"progresso": 85, "status": "Excelente", "cor": "#2ECC71"},
        "Potenciação": {"progresso": 42, "status": "Crítico", "cor": "#FF4B4B"},
        "Geometria": {"progresso": 60, "status": "Estável", "cor": "#FFA500"}
    }

    # Seletor para o gráfico dinâmico
    col_sel, _ = st.columns([1, 2])
    with col_sel:
        topico = st.selectbox("Analisar evolução de:", list(meus_assuntos.keys()))

    # Gráfico de Evolução (Histórico do aluno no tópico)
    df_evolucao = pd.DataFrame({
        "Data": ["01/Mai", "05/Mai", "10/Mai", "15/Mai", "20/Mai"],
        "Meu Nível": [10, 25, 45, 40, meus_assuntos[topico]["progresso"]]
    })
    
    fig = px.area(df_evolucao, x="Data", y="Meu Nível", 
                  title=f"Minha Evolução em {topico}",
                  color_discrete_sequence=[meus_assuntos[topico]["cor"]])
    fig.update_layout(yaxis_range=[0,105], height=300)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # --- 4. LISTA DE TÓPICOS ---
    st.subheader("Meus Tópicos")
    
    c_h1, c_h2, c_h3, c_h4 = st.columns(4)
    with c_h1: st.caption("TÓPICO")
    with c_h2: st.caption("MEU PROGRESSO")
    with c_h3: st.caption("SITUAÇÃO")
    with c_h4: st.caption("DETALHES")
    st.divider()

    for nome, info in meus_assuntos.items():
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown(f"**{nome}**")
        with c2:
            st.progress(info["progresso"] / 100)
        with c3:
            st.markdown(f"{status_dot(info['cor'])} {info['status']}", unsafe_allow_html=True)
        with c4:
            st.page_link("pages/Melhorar.py", label="Melhorar")
        st.write("")

if __name__ == "__main__":
    card_aluno()