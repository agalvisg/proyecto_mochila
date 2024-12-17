import requests

def obtener_clima(ciudad, api_key="edd57683ac77400b3b1ad0bfd57a6b77"):
    """
    Consulta el clima de una ciudad utilizando la API de OpenWeather.
    :param ciudad: Nombre de la ciudad
    :param api_key: Clave de la API
    :return: Clima actual (descripción y temperatura)
    """
    url_base = "http://api.openweathermap.org/data/2.5/weather?"
    url = url_base + "appid=" + api_key + "&q=" + ciudad + "&units=metric"

    # Realizamos la solicitud HTTP
    response = requests.get(url)
    
    if response.status_code == 200:  # Verificar el código de estado
        data = response.json()  # Convertir la respuesta en JSON
        descripcion = data["weather"][0]["description"]
        temperatura = data["main"]["temp"]
        return descripcion, temperatura
    elif response.status_code == 404:  # Ciudad no encontrada
        return f"No se encontró la ciudad: {ciudad}"
    elif response.status_code == 401:  # API Key inválida
        return "Error 401: La clave API no es válida."
    else:  # Otros errores
        return f"Error al consultar el clima: {response.status_code}"

# Prueba con una ciudad
try:
    ciudad = "Lima"
    clima = obtener_clima(ciudad)
    if isinstance(clima, tuple):
        print(f"El clima en {ciudad} es {clima[0]} con una temperatura de {clima[1]}°C.")
    else:
        print(clima)
except Exception as e:
    print(f"Error: {e}")
