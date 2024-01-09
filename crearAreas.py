from classes.classAreas import *
from processJsonToMain import *

areas['Apolo'] = areasEntrenamiento('Apolo',ruta='Ruta Java')
areas['Artemis'] = areasEntrenamiento('Artemis',ruta='Ruta NetCore')
areas['Sputnik'] = areasEntrenamiento('Sputnik',ruta='Ruta NodeJS')


for i in areas:
  crearJson(areas[i],f"{CARPETAS[1]}{i}.json")