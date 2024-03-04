import requests
from bs4 import BeautifulSoup

url = 'https://corre.cl/'

# Realiza una petición GET a la página
response = requests.get(url)
response.raise_for_status()  # Asegura que la petición fue exitosa

# Parsea el contenido HTML de la página
soup = BeautifulSoup(response.text, 'html.parser')

# Encuentra el contenedor que tiene el id "meses"
events_container = soup.find(id="meses")

# Verifica si el contenedor existe y busca dentro los divs correspondientes a month-1 y month-2
if events_container:
    for month_number in range(1, 3):  # Esto iterará sobre month-1 y month-2
        month_events = events_container.find_all(class_=f'month-{month_number}')

        for event in month_events:
            # Extrae la fecha del evento
            fecha = event.find(class_='day-header').get_text(strip=True)
            
            # Encuentra el enlace del detalle del evento y extrae la URL
            event_detail_link = event.find('a')['href']
            
            # Extrae el nombre del evento
            nombre = event.find(class_='e-name').get_text(strip=True)
            
            # Extrae la dirección del evento
            direccion = event.find(class_='e-data').get_text(strip=True)
            
            print(f'Fecha: {fecha}, Nombre: {nombre}, Dirección: {direccion}, Link de detalle: {event_detail_link}')
else:
    print("No se encontró el contenedor de eventos.")
