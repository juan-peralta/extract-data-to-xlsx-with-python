import pandas as pd

# Carga una hoja específica del archivo Excel en un DataFrame
df = pd.read_excel(r"listado_aranceles_de_referencia_2024_cft-ip-ffaa_12012024.xlsx", sheet_name='Arancel Refer CFT-IP 2024')

# Muestra las primeras 7 filas de esa hoja
print(df.head(7))


# Transforma todo el DataFrame a JSON
json_data = df.to_json(orient='records', lines=True)

# Imprime el JSON
print(json_data)