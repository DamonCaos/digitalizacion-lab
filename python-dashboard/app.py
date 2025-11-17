"""
Dashboard industrial de ejemplo.
Requisitos recomendados:
  pip install pandas plotly dash
"""

import pandas as pd
from datetime import datetime, timedelta

# Si usas Dash:
# from dash import Dash, dcc, html
# import plotly.express as px

def load_sample_data():
    """Genera datos simulados de producción para pruebas."""
    now = datetime.now().replace(second=0, microsecond=0)
    records = []
    for i in range(0, 8 * 60, 5):  # cada 5 minutos durante 8 horas
        ts = now - timedelta(minutes=i)
        linea = 1
        ref = "SG-12345"
        piezas_buenas = 100 + (i % 20)
        piezas_scrap = (i % 7)
        records.append(
            {
                "FechaHora": ts,
                "Linea": linea,
                "Referencia": ref,
                "PiezasBuenas": piezas_buenas,
                "PiezasScrap": piezas_scrap,
            }
        )
    df = pd.DataFrame(records)
    return df.sort_values("FechaHora")

def main():
    df = load_sample_data()
    print("Ejemplo de datos de producción:")
    print(df.head())

    # Aquí puedes montar tu lógica de dashboard con Dash o Streamlit.
    # Ejemplo Dash simplificado (descomenta si quieres usarlo):
    #
    # app = Dash(__name__)
    # fig = px.line(
    #     df,
    #     x="FechaHora",
    #     y=["PiezasBuenas", "PiezasScrap"],
    #     title="Producción vs Scrap (simulado)"
    # )
    #
    # app.layout = html.Div(
    #     children=[
    #         html.H1("Dashboard Industrial · Ejemplo"),
    #         dcc.Graph(id="produccion-graph", figure=fig),
    #     ]
    # )
    #
    # app.run_server(debug=True)

if __name__ == "__main__":
    main()
