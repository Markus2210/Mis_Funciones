def sumar_digitos(numero: int)-> int:
    total = 0
    if numero < 10:
        return numero
    else:
        return (numero % 10) + sumar_digitos (numero//10)
                #Me da el resto                 #me da el número
                #de dividir el                  #redondeado para abajo
                #número por 10
    
print(sumar_digitos(1234))