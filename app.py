import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Portfolio Guardian",
    page_icon="🛡️",
    layout="wide"
)

# -----------------------------
# CABECERA
# -----------------------------
st.title("🛡️ Portfolio Guardian")
st.subheader("Centro de Decisiones")

st.write(f"**Última actualización:** {datetime.now().strftime('%d/%m/%Y %H:%M')}")

st.divider()

# -----------------------------
# INDICADORES
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("IRM", "72 / 100", "🟢")

with col2:
    st.metric("Mercado", "Alcista")

with col3:
    st.metric("Riesgo", "Moderado")

st.divider()

# -----------------------------
# COMITÉ DE INVERSIÓN
# -----------------------------
st.header("Comité de Inversión")

col1, col2 = st.columns(2)

with col1:
    st.success("✔ Tendencia")
    st.success("✔ Opciones")
    st.success("✔ Crédito")

with col2:
    st.warning("⚠ Sentimiento")
    st.success("✔ Macro")

st.divider()

# -----------------------------
# RECOMENDACIÓN
# -----------------------------
st.header("Recomendación")

st.info("""
**Mantener la cartera actual.**

Las nuevas aportaciones deberían dirigirse, por ahora, a un **fondo monetario**.

Todavía no existen señales suficientes para reducir el riesgo.
""")

st.divider()

st.caption("Portfolio Guardian v0.1")
