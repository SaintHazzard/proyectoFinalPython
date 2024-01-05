from persona import *

registroAspirantes = {}
rutas={
  
}
registroAspirantes['0']= Camper('1097910340', 'Oviel Felipe', 'Mendoza Pineda',3165880900,123123456, 'Cir 36a 104-128 Altos de la Pradera T3-1204', 'Martiza Pineda Celis', 'Aspirante','')
registroAspirantes['1'] = Camper('1098808399','Alejandro','Martinez Santos',3214321455,8883599,'Monviso','Mi madresita','Aspirante','')

for i in registroAspirantes:
  print('-'*50)
  registroAspirantes[i].showData()
  


registroAspirantes['0'].crearJson()
registroAspirantes['1'].crearJson()
