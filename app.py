import streamlit as st
from collections import defaultdict
from calculos import decompor_formula, calcular_forca_ionica
from constantes import CARGAS, COMPOSTOS_IONICOS

# Configuração da página
st.set_page_config(
    page_title="Calculadora de Força Iônica",
    page_icon="🧪",
    layout="centered"
)

# Estado inicial
if "compostos" not in st.session_state:
    st.session_state.compostos = []

# === INTERFACE STREAMLIT ===
st.title("🧪 Calculadora de Força Iônica 🧪")

# Formulário para adicionar compostos
with st.form("adicionar_composto"):
    col1, col2 = st.columns([2, 1])
    with col1:
        formula = st.text_input(
            "Fórmula do composto (ex: NaCl, NH4OH)",
            placeholder="NaCl",
            help="Digite a fórmula química do composto"
        ).strip()
    with col2:
        conc_input = st.text_input(
            "Concentração (mol/L)",
            placeholder="0.1",
            help="Use ponto como separador decimal"
        ).replace(",", ".").strip()

    adicionar = st.form_submit_button("➕ Adicionar composto")

    if adicionar:
        if formula and conc_input:
            try:
                conc_valor = float(conc_input)
                if conc_valor < 0:
                    st.error("A concentração não pode ser negativa.")
                else:
                    st.session_state.compostos.append((formula, conc_valor))
                    st.success(f"Composto adicionado: {formula} ({conc_valor} mol/L)")
            except ValueError:
                st.error("Concentração inválida. Use ponto como separador decimal.")
        else:
            st.warning("Preencha os dois campos antes de adicionar.")

# Lista de compostos adicionados
if st.session_state.compostos:
    st.subheader("📋 Compostos adicionados:")
    
    # Mostrar em formato de tabela
    for i, (f, c) in enumerate(st.session_state.compostos):
        cols = st.columns([4, 1, 1])
        cols[0].write(f"**{f}**")
        cols[1].write(f"{c} mol/L")
        if cols[2].button("🗑️", key=f"del_{i}"):
            st.session_state.compostos.pop(i)
            st.rerun()

    # Botões de ação
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("✅ Calcular Força Iônica", type="primary"):
            try:
                mu = calcular_forca_ionica(st.session_state.compostos)
                st.success(f"💡 Força Iônica total: **{mu:.4f} mol/L**")
            except ValueError as e:
                st.error(str(e))
    with col2:
        if st.button("🗑️ Limpar tudo", type="secondary"):
            st.session_state.compostos.clear()
            st.rerun()
    with col3:
        if st.button("📋 Exemplos rápidos"):
            st.session_state.compostos = [("NaCl", 0.1), ("CaCl2", 0.05)]
            st.rerun()

# Mensagem quando não há compostos
if not st.session_state.compostos:
    st.info("ℹ️ Nenhum composto adicionado ainda. Use o formulário acima ou clique em 'Exemplos rápidos'.")
