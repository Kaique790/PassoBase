import streamlit as st

st.set_page_config(page_title="Reforço de Conteúdo", layout="wide")

# Botão de retorno simples
st.page_link("Início.py", label="<- Voltar para Minhas Jornada")


# Simulação de conteúdo dinâmico (aqui poderia vir de um banco de dados)
# Vamos usar 'Potenciação' como exemplo, que era o foco de atenção no Dashboard
st.title("Reforço Acadêmico: Potenciação")
st.divider()

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Resumo Teórico")
    st.write("""
    A potenciação representa a multiplicação de um número (base) por ele mesmo várias vezes, 
    conforme indicado pelo expoente.
    """)
    
    st.markdown("""
    **Regras Fundamentais:**
    
    1. **Produto de bases iguais:** Mantém a base e soma os expoentes.
    2. **Divisão de bases iguais:** Mantém a base e subtrai os expoentes.
    3. **Potência de potência:** Mantém a base e multiplica os expoentes.
    4. **Expoente zero:** Todo número (exceto zero) elevado a zero é igual a 1.
    """)
    
    st.info("""
    **Dica de Estudo:**
    Cuidado com os parênteses! (-2)² é diferente de -2². 
    No primeiro caso, o resultado é 4. No segundo, é -4.
    """)

with col2:
    st.subheader("Prática Imediata")
    st.write("Resolva as questões abaixo para validar seu entendimento:")
    
    # Questão 1
    st.markdown("---")
    st.markdown("**Questão 1**")
    st.write("Qual é o valor da expressão (2³ * 2²)?")
    q1 = st.radio("Selecione a alternativa correta:", ["10", "32", "64", "12"], key="q1", label_visibility="collapsed")
    
    if st.button("Verificar Questão 1"):
        if q1 == "32":
            st.success("Correto! 2³ * 2² = 2⁵ = 32.")
        else:
            st.error("Tente novamente. Lembre-se de somar os expoentes: 3 + 2 = 5.")

    # Questão 2
    st.markdown("---")
    st.markdown("**Questão 2**")
    st.write("Determine o valor de (5² * 2⁰):")
    q2 = st.number_input("Digite o resultado numérico:", step=1, key="q2")
    
    if st.button("Verificar Questão 2"):
        if q2 == 25:
            st.success("Exato! 5² é 25 e qualquer número elevado a zero é 1. Portanto, 25 * 1 = 25.")
        else:
            st.warning("Dica: Resolva primeiro a potência de base 5 e depois a de base 2.")

st.divider()

# Rodapé de incentivo
st.subheader("Próximos Passos")
st.write("""
Após concluir estas questões, recomendamos que você refaça os exercícios da lista oficial da semana 
para consolidar o aprendizado e subir seu nível de proficiência no gráfico geral.
""")