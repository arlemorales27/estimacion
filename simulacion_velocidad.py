# semana1_calculadora.py

# 1. Importar la librería pandas
import pandas as pd

# Nombre del archivo de Excel
archivo_excel = 'presupuesto_proyecto_v1.xlsx'
nombre_hoja = 'CostosDirectos'

print(f"--- Leyendo el archivo: {archivo_excel} ---")

# 2. Leer el archivo Excel usando pandas
#    pd.read_excel() lee los datos y los convierte en un DataFrame.
#    Un DataFrame es como una tabla de Excel dentro de Python.
try:
    df_costos = pd.read_excel(archivo_excel)

    # 3. Mostrar los datos leídos para verificar
    print("\nDatos leídos desde Excel:")
    print(df_costos)

    # 4. Calcular la columna 'Costo Total (COP)'
    #    Multiplicamos la columna 'Horas Estimadas' por 'Tarifa por Hora (COP)'
    df_costos['Costo Total (COP)'] = df_costos['Horas Estimadas'] * df_costos['Tarifa por Hora (COP)']

    # 5. Calcular el costo total del proyecto
    #    Sumamos todos los valores de la nueva columna 'Costo Total (COP)'
    costo_total_proyecto = df_costos['Costo Total (COP)'].sum()

    # 6. Mostrar los resultados finales
    print("\n--- Presupuesto Calculado ---")
    print("\nDetalle de costos por tarea:")
    print(df_costos)

    print("\n-----------------------------------------------------")
    # Usamos f-strings para formatear el número como moneda
    print(f"Costo Total Directo del Proyecto: ${costo_total_proyecto:,.2f} COP")
    print("-----------------------------------------------------")

except FileNotFoundError:
    print(f"\n¡ERROR! No se encontró el archivo '{archivo_excel}'.")
    print("Asegúrate de que el archivo esté en la misma carpeta que el script.")