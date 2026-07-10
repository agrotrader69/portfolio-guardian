import pandas as pd

def calculate_irm(data):
    """
    Calcula un Indicador de Riesgo de Mercado (IRM) básico.
    """

    score = 50

    # VIX
    if "VIX" in data:
        vix = data["VIX"]["precio"]

        if vix < 20:
            score += 20
        elif vix < 30:
            score += 5
        else:
            score -= 20

    # S&P500
    if "S&P 500" in data:
        cambio = data["S&P 500"]["cambio"]

        if cambio > 0:
            score += 10
        else:
            score -= 10

    score = max(0, min(score,100))

    return score
