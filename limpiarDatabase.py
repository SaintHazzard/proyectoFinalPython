import os



CARPETAS = ['jsonData/','jsonDataAreas/','jsonDataRutas/']


for carp in CARPETAS:
  if os.path.exists(carp):
    archivosDentro = os.listdir(carp)
  for archivo in archivosDentro:
    rutaCompleta = os.path.join(carp,archivo)
    try:
      if os.path.isfile(rutaCompleta):
        os.remove(rutaCompleta)
        print(f"Archivo {rutaCompleta} eliminado.")
    except Exception as e:
      print(f"Error al eliminar {rutaCompleta}: {e}")
  else:
    print(f"La carpeta {carp} no existe.")