import streamlit as st

# Configuração da página inicial
st.set_page_config(page_title="PassoBase - Login", layout="centered")

st.title("PassoBase")
st.subheader("Bem-vindo! Como você deseja acessar o portal?")

st.divider()

# Criando duas colunas para os botões de acesso
col1, col2 = st.columns(2)

with col1:
    st.info("### Portal do Aluno")
    st.write("Acesse suas jornadas, trilhas de reforço e acompanhe sua evolução.")
    # Redireciona para o Início do aluno
    if st.button("Acessar como Aluno", use_container_width=True, type="primary"):
        st.switch_page("pages/Painel_do_Aluno.py")

with col2:
    st.success("### Painel do Professor")
    st.write("Gerencie suas turmas, visualize diagnósticos e acompanhe o desempenho geral.")
    # Redireciona para o Início do professor
    if st.button("Acessar como Professor", use_container_width=True):
        st.switch_page("pages/Painel_do_Professor.py")

st.divider()
st.caption("PassoBase - Sistema de Diagnóstico de Aprendizado © 2026")