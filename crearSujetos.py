from classes.classCamper import *
registroAspirantes={}




registroAspirantes['1'] = Camper('1',
                                  'Alejandro',
                                  'Martinez Santos',
                                  3214321455,
                                  8883599,
                                  'Monviso',
                                  'Mi madresita')
registroAspirantes['0']= Camper('0', 'Oviel Felipe', 'Mendoza Pineda',315880000,123123456, 'Direccion: El weon se doxea solo', 'Martiza Pineda Celis')






registroAspirantes['2']= Camper('2', 'Oviel 2', 'Mendoza Pineda',3165880000,123123456, 'Direccion: El weon se doxea solo', 'Martiza Pineda Celis')

registroAspirantes['3']= Camper('3', 'Sofia Marcela', 'Medina Diaz',3165881111,123123456 , 'Tandamandapio', 'Jaimito el cartero')

registroAspirantes['1'] = Camper('1',
                                  'Alejandro',
                                  'Martinez Santos',
                                  3214321455,
                                  8883599,
                                  'Monviso',
                                  'Mi madresita')

for i in registroAspirantes:
  registroAspirantes[i].crearJson()