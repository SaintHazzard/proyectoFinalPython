from persona import *

registroAspirantes = {}
rutas={
  
}
registroAspirantes['1097910340']= Camper('1097910340', 'Oviel Felipe', 'Mendoza Pineda', 3165880900, 'Cir 36a 104-128 Altos de la Pradera T3-1204', 'Martiza Pineda Celis', 'Aspirante','')
registroAspirantes['1098808399'] = Camper('1098808399','Alejandro','Martinez Santos',3214321455,'Monviso','Mi madresita','Aspirante','')

for i in registroAspirantes:
  print('-'*50)
  registroAspirantes[i].showData()