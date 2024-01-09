from classes.classRutas import *
from  processJsonToMain import *
rutas = {}
modfundamentos = Modulo("Fundamentos de programación", ["Introducción a la algoritmia", "PSeInt", "Python"]).getModulo()
modweb = Modulo("Programación Web", ["HTML", "CSS", "Bootstrap"]).getModulo()
modformal = Modulo("Programación formal", ["Java", "JavaScript", "C#"]).getModulo()
modbackend = Modulo("Backend", ["NetCore", "Spring Boot", "NodeJS", "Express"]).getModulo()
# modbd = Modulo("Bases de datos", ["MySQL", "MongoDB", "PostgreSQL"]).getModulo()


rutas["Ruta NodeJS"] = RutaEntrenamiento("Ruta NodeJS", {"fundamentos": modfundamentos, "web": modweb, "formal" : modformal, "backend": modbackend}, "MySQL", "MongoDB")
rutas["Ruta Java"] = RutaEntrenamiento("Ruta Java", {"fundamentos": modfundamentos, "formal" : modformal, "backend": modbackend}, "PostgreSQL", "MongoDB")
rutas["Ruta NetCore"] = RutaEntrenamiento("Ruta NetCore", {"formal" : modformal, "backend": modbackend}, "MySQL", "MongoDB")
rutas["Desarrollo Backend"] = RutaEntrenamiento("Desarrollo Backend", {"fundamentos": modfundamentos, "formal" : modformal, "backend": modbackend}, "PostgreSQL", "MySQL")

for i in rutas:
  crearJson(rutas[i],f"{CARPETAS[2]}{i}.json")
  
  
  
  
# RutaEntrenamiento.printRutaEntrenamiento(rutas["Desarrollo Backend"],[modfundamentos, modweb])