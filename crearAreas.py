from classes.classAreas import *
from processJsonToMain import *

areas['Apolo'] = areasEntrenamiento('Apolo')
areas['Artemis'] = areasEntrenamiento('Artemis')
areas['Sputnik'] = areasEntrenamiento('Sputnik')


for i in areas:
  crearJson(areas[i],f"{CARPETAS[1]}{i}.json")