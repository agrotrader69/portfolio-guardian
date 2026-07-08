import streamlit as st

# Configuración de página
st.set_page_config(
    page_title="Portfolio Guardian",
    page_icon="📊",
    layout="wide"
)

# Título
st.title("📊 Portfolio Guardian")

st.write(
    "Sistema de análisis de riesgo de mercado y gestión de cartera."
)

st.divider()

# Indicador provisional
irm = 75

# Estado del mercado
if irm >= 70:
    estado = "🟢 Riesgo bajo / Mercado estable"
elif irm >= 40:
    estado = "🟠 Precaución"
else:
    estado = "🔴 Riesgo elevado"

# Mostrar indicadores
col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Indicador de Riesgo de Mercado (IRM)",
        f"{irm}/100"
    )

with col2:
    st.metric(
        "Estado actual",
        estado
    )

st.divider()

st.subheader("Asignación defensiva propuesta")

datos = {
    "Fondos indexados": "50%",
    "Fondos monetarios": "20%",
    "Oro": "10%",
    "Retorno absoluto": "10%",
    "Liquidez": "10%"
}

for activo, porcentaje in datos.items():
    st.write(f"**{activo}:** {porcentaje}")

st.divider()

st.subheader("Próximos módulos")

st.write("""
✅ VIX  
✅ Sentimiento AAII  
✅ Fear & Greed  
✅ S&P 500  
✅ MSCI World  
✅ Crédito  
✅ Indexa  
✅ Finizens  
✅ MyInvestor  
✅ Trade Republic  
""")
