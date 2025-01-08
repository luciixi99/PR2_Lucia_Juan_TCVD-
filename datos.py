import openai
import pandas as pd
import chardet
# Specify the path to your CSV file
file_path = "unique_amenities.csv"

#configure openai key
df = pd.read_csv('unique_amenities.csv', encoding='ISO-8859-1')
df = df['amenities'].to_list()


# Construye el prompt
prompt = f"""
Tienes una lista de "amenities" de alojamientos. Categorízalas en las siguientes subcategorías:
1. Acceso a Espacios y Áreas Comunes
2. Confort y Climatización
3. Mobiliario y Espacios de Relajación
4. Cocina y Equipos
5. Electrodomésticos y Equipos de Tecnología
6. Servicios y Seguridad
7. Baño y Higiene
8. Niños y Familia
9. Actividades y Entretenimiento
10. Accesorios y Otros
11. Vistas
12. Estacionamiento (Parking)

Lista de amenities:
{', '.join(df)}

Devuelve un resultado en formato JSON donde cada amenity esté asignada a una categoría.
"""

# Llama a la API con el nuevo modelo de chat
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Puedes usar "gpt-4" si lo tienes acceso
    messages=[
        {"role": "system", "content": "Eres un asistente que categoriza amenities de alojamientos."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=200,
    temperature=0
)

# Imprime el resultado
print(response['choices'][0]['message']['content'])




