import requests

BASE_URL = "https://botardo.onrender.com"
#BASE_URL = "http://0.0.0.0:5001"


def get_home():
  # A GET request to the API
  response = requests.get(BASE_URL)

  # Print the response
  response_json = response.json()
  print(response_json)
  return response_json


def get_student(dni):
  # A GET request to the API
  response = requests.get(f"{BASE_URL}/v1/student?dni={dni}")

  # Print the response
  response_json = response.json()
  print(response_json)
  return response_json


def register_student(identificador, discord_id):
  # A GET request to the API
  data = {'discord_id': str(discord_id), 'identificador': identificador}
  try:
    response = requests.put(f"{BASE_URL}/v1/student/register", json=data)

    # Print the response

    response_json = response.json()
    return response_json
  except:
    return {'code': -1}


def obtener_aprobados():
  # A GET request to the API
  response = requests.get(f"{BASE_URL}/v1/student/approved")

  # Print the response
  response_json = response.json()
  return response_json
