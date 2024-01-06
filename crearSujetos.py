from classes.classCamper import *
registroAspirantes={}
registroAspirantes['1']= Camper('1', 'Oviel Felipe', 'Mendoza Pineda',3165880900,123123456, 'Cir 36a 104-128 Altos de la Pradera T3-1204', 'Martiza Pineda Celis')


registroAspirantes['0'] = Camper('0',
                                  'Alejandro',
                                  'Martinez Santos',
                                  3214321455,
                                  8883599,
                                  'Monviso',
                                  'Mi madresita')



registroAspirantes['2']= Camper('2', 'Oviel 2', 'Mendoza Pineda',3165880900,123123456, 'Cir 36a 104-128 Altos de la Pradera T3-1204', 'Martiza Pineda Celis')

registroAspirantes['3']= Camper('3', 'Sofia Marcela', 'Medina Diaz',3165880900,123123456 , 'Cir 36a 104-128 Altos de la Pradera T3-1204', 'Martiza Pineda Celis')



for i in registroAspirantes:
  registroAspirantes[i].crearJson()