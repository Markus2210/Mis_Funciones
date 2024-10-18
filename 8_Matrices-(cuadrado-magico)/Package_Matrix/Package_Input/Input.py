from .Validate import validate_number, validate_lenght

def get_int(mensaje:str,mensaje_error:str,minimo:int,maximo:int,reintentos:int):
    
    for _ in range(reintentos):
        user_input = int(input(mensaje))
        numero = validate_number(user_input,minimo,maximo)
        if numero is not None:
            return numero
        else: 
            print(mensaje_error)
    return None

def get_float(mensaje:str,mensaje_error:str,minimo:float,maximo:float,reintentos:int):
    
    for _ in range(reintentos):
        user_input = float(input(mensaje))
        numero = validate_number(user_input,minimo,maximo)
        if numero is not None:
            return numero
        else: 
            print(mensaje_error)
    return None

def get_str(mensaje:str,mensaje_error:str, longitud:int) -> str|None: 
    user_input = str(input(mensaje))
    string = validate_lenght(user_input,longitud)
    if string is not None:
        return string
    else: 
        print(mensaje_error)
    
    return None
