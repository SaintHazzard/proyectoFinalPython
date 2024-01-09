from typing import overload

@overload
def ejemplo(arg: int) -> str:
    ...

@overload
def ejemplo(arg: str) -> int:
    ...

def ejemplo(arg):
    # Implementación real de la función
    if isinstance(arg, int):
        return str(arg)
    elif isinstance(arg, str):
        return int(arg)
      
