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

# ==========================
# DATOS DE MERCADO
# ==========================

datos = get_market_data()

st.header("Mercado")

col1, col2 = st.columns(2)

i = 0

for nombre, valor in datos.items():

    if i % 2 == 0:
        with col1:
            st.metric(
                nombre,
                valor["precio"],
                f'{valor["cambio"]}%'
            )
    else:
        with col2:
            st.metric(
                nombre,
                valor["precio"],
                f'{valor["cambio"]}%'
            )

    i += 1

st.divider()

st.header("Centro de Decisiones")

st.success("🟢 Mercado en seguimiento")

st.info("""
De momento esta versión solo muestra datos reales del mercado.

En la siguiente versión se incorporarán:

- VIX
- Fear & Greed
- Put/Call Ratio
- AAII
- Comité de Inversión
- Recomendación automática
""")
