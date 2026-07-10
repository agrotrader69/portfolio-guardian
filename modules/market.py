import yfinance as yf


def get_market_data():
    """
    Descarga datos básicos de mercado.
    """

    activos = {
        "S&P 500": "^GSPC",
        "Nasdaq": "^IXIC",
        "VIX": "^VIX",
        "Oro": "GC=F"
    }

    datos = {}

    for nombre, ticker in activos.items():
        try:
            activo = yf.Ticker(ticker)
            hist = activo.history(period="2d")

            if len(hist) >= 2:
                cierre = hist["Close"].iloc[-1]
                anterior = hist["Close"].iloc[-2]

                cambio = ((cierre - anterior) / anterior) * 100

                datos[nombre] = {
                    "precio": round(cierre, 2),
                    "cambio": round(cambio, 2)
                }

        except Exception:
            datos[nombre] = {
                "precio": None,
                "cambio": None
            }

    return datos
