import requests as requests

def obtener_clima(ciudad, api_key="TU_API_KEY"):
    """
    Consulta el clima de una ciudad utilizando la API de OpenWeather.
    :param ciudad: Nombre de la ciudad
    :param api_key: Clave de la API
    :return: Clima actual (descripción y temperatura)
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&units=metric&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        descripcion = data["weather"][0]["description"]
        temperatura = data["main"]["temp"]
        return descripcion, temperatura
    else:
        raise Exception(f"Error al consultar el clima: {response.status_code}")
