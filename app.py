import streamlit as st
from datetime import datetime
from modules.market import get_market_data

st.set_page_config(
    page_title="Portfolio Guardian",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Portfolio Guardian")
st.subheader("Centro de Decisiones")

st.write(f"Actualizado: {datetime.now().strftime('%d/%m/%Y %H:%M')}")

st.divider()

try:
    datos = get_market_data()

    st.header("Mercado")

    col1, col2 = st.columns(2)

    items = list(datos.items())

    for i, (nombre, valor) in enumerate(items):
        with col1 if i % 2 == 0 else col2:
            st.metric(
                label=nombre,
                value=valor["precio"],
                delta=f'{valor["cambio"]}%'
            )

except Exception as e:
    st.error(f"Error obteniendo datos: {e}")

st.divider()

st.header("Centro de Decisiones")

st.success("🟢 Mercado en seguimiento")

st.info(
    """
Esta es la primera versión de Portfolio Guardian.

Próximamente incorporaremos:

- VIX
- Fear & Greed
- Put/Call Ratio
- AAII
- Comité de Inversión
- Recomendaciones automáticas
"""
)
