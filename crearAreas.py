from classes.classAreas import *


areas['Apolo'] = areasEntrenamiento('Apolo')
areas['Artemis'] = areasEntrenamiento('Artemis')
areas['Sputnik'] = areasEntrenamiento('Sputnik')
for i in areas:
  areas[i].crearJson()