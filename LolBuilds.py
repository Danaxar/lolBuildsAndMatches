# Programa para buscar builds de lol
import requests
import psutil


# Variables globales
linkInicial = "https://porofessor.gg/es/live/"

# Objetos
'''
class Config:
    def __init__():
        this.nickname = 
'''


# Funciones
def leerConfig():
    archivo_config = open("config.txt", "r")
    salida = archivo_config.readlines()
    print("Configuraciones:\n", salida)
    return salida

def isJuegoActivo():
    '''Función que evalúa si el juego se está ejecutando en el sistema'''
    return "League of Legends.exe" in (p.name() for p in psutil.process_iter())

def arreglarNickNameRequest(playerName):
    if " " in playerName:
        playerName = playerName.replace(" ", "%20")
    return playerName
    

def hacerRequest(servidor, playerName):
    '''Funcion que hace el request de la página de info
    servidor = nombre del servidor en minuscula (las)
    '''
    link = linkInicial + servidor + "/" + arreglarNickNameRequest(playerName)
    print("Haciendo request: ", link)
    # Hacer el request
    page = requests.get(link)
    stringPage = page.text
    print(stringPage)
    return

# Main

# Leer archivos de configuracion
print("Iniciando lolBuilds.py...")
stringConfig = leerConfig()
print(hacerRequest("las", "walala del colo"))

'''
encendido = True
while encendido:
    # Buscar actividad de lol
    if isJuegoActivo():
        # Detectar campeón de lol
        # Buscar build
        # Abrir navegador

    sleep(20)
'''

