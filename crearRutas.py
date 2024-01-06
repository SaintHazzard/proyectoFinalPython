from classes.classRutas import *
modfundamentos = Modulo("Fundamentos de programación", ["Introducción a la algoritmia", "PSeInt", "Python"]).showModulo()
modweb = Modulo("Programación Web", ["HTML", "CSS", "Bootstrap"]).showModulo()
modformal = Modulo("Programación formal", ["Java", "JavaScript", "C#"]).showModulo()
modbd = Modulo("Bases de datos", ["MySQL", "MongoDB", "PostgreSQL"]).showModulo()
modbackend = Modulo("Backend", ["NetCore", "Spring Boot", "NodeJS", "Express"]).showModulo()


rutas["Programación Web"] = RutaEntrenamiento("Programación Web", [modfundamentos, modweb], "MySQL", "MongoDB")
rutas["Desarrollo Backend"] = RutaEntrenamiento("Desarrollo Backend", [modfundamentos, modweb, modformal, modbd, modbackend], "PostgreSQL", "MongoDB")

for i,k in enumerate(rutas):
  rutas[k].crearJson()
  
# RutaEntrenamiento.printRutaEntrenamiento(rutas["Desarrollo Backend"],[modfundamentos, modweb])