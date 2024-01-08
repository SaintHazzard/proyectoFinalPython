from classes.classRutas import *
from  processJsonToMain import *
rutas = {}
modfundamentos = Modulo("Fundamentos de programación", ["Introducción a la algoritmia", "PSeInt", "Python"]).getModulo()
modweb = Modulo("Programación Web", ["HTML", "CSS", "Bootstrap"]).getModulo()
modformal = Modulo("Programación formal", ["Java", "JavaScript", "C#"]).getModulo()
modbackend = Modulo("Backend", ["NetCore", "Spring Boot", "NodeJS", "Express"]).getModulo()
# modbd = Modulo("Bases de datos", ["MySQL", "MongoDB", "PostgreSQL"]).getModulo()


rutas["Ruta NodeJS"] = RutaEntrenamiento("Ruta NodeJS", [modfundamentos, modweb, modformal,modbackend], "MySQL", "MongoDB")
rutas["Ruta Java"] = RutaEntrenamiento("Ruta Java", [modfundamentos, modformal, modbackend], "PostgreSQL", "MongoDB")
rutas["Ruta NetCore"] = RutaEntrenamiento("Ruta NetCore", [modformal, modbackend], "MySQL", "MongoDB")
rutas["Desarrollo Backend"] = RutaEntrenamiento("Desarrollo Backend", [modfundamentos, modformal, modbackend], "PostgreSQL", "MySQL")

for i in rutas:
  crearJson(rutas[i],f"{CARPETAS[2]}{i}.json")
  
  
  
  
# RutaEntrenamiento.printRutaEntrenamiento(rutas["Desarrollo Backend"],[modfundamentos, modweb])