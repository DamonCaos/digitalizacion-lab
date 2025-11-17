    """
    Script de informe diario de producción (plantilla).

    Requisitos:
      pip install pandas sqlalchemy

    NOTA: ajusta la cadena de conexión y nombres de tabla a tu entorno real.
    """

    from datetime import datetime, timedelta
    import pandas as pd
    from sqlalchemy import create_engine

    # Ejemplo de cadena de conexión (ajusta a tu servidor):
    # engine = create_engine("mssql+pyodbc://USUARIO:PASS@SERVIDOR/Produccion?driver=ODBC+Driver+17+for+SQL+Server")
    engine = None  # Sustituye por tu engine real

    def load_daily_data(day=None):
        if day is None:
            day = datetime.now().date()
        if engine is None:
            # Modo demo sin base real
            print("Engine no configurado. Modo demo.")
            data = {
                "Linea": [1, 1, 1],
                "Referencia": ["SG-12345", "SG-12345", "SG-67890"],
                "PiezasBuenas": [1000, 980, 1100],
                "PiezasScrap": [25, 30, 15],
            }
            return pd.DataFrame(data)

        start = datetime.combine(day, datetime.min.time())
        end = start + timedelta(days=1)

        query = f"""
        SELECT Linea, Referencia, PiezasBuenas, PiezasScrap
        FROM Produccion
        WHERE FechaHora >= '{start}' AND FechaHora < '{end}'
        """
        return pd.read_sql(query, engine)

    def generate_report(df: pd.DataFrame, output_path: str):
        resumen = df.groupby(["Linea", "Referencia"]).sum(numeric_only=True)
        resumen["Scrap_%"] = resumen["PiezasScrap"] / (resumen["PiezasBuenas"] + resumen["PiezasScrap"]) * 100

        lines = []
        lines.append("=== Informe diario de producción (demo) ===
")
        lines.append(resumen.to_string())
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("
".join(lines))

        print(f"Informe generado en: {output_path}")

    def main():
        df = load_daily_data()
        generate_report(df, "informe_diario.txt")

    if __name__ == "__main__":
        main()
