def ingresar_puntuacion():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5:')
        point = input()
        
        if point.isdecimal():
            point = int(point)
            if point < 1 or point > 5:
                print('Por favor, introduzca un valor entre 1 y 5.')
            else:
                print('Por favor, introduzca un comentario:')
                comment = input()
                post = f'punto: {point} comentario: {comment}'
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post}\n')
                break
        else:
            print('Por favor, introduzca la puntuación en números.')

def comprobar_resultados():
    print('Resultados hasta la fecha:')
    try:
        with open("data.txt", "r") as read_file:
            resultados = read_file.read()
            if resultados:
                print(resultados)
            else:
                print('No hay resultados.') 
    except FileNotFoundError:
        print('No hay resultados.') #no se ve los resltads

def main():
    while True:
        print('Seleccione el proceso que desea aplicar:')
        print('1: Ingresar puntuación y comentario')
        print('2: Comprobar los resultados obtenidos hasta ahora.')
        print('3: Finalizar')
        num = input()
        
        if num.isdecimal():
            num = int(num)
            if num == 1:
                ingresar_puntuacion()
            elif num == 2:
                comprobar_resultados()
            elif num == 3:
                print('Finalizando...')
                break
            else:
                print('Por favor, introduzca un número del 1 al 3.')
        else:
            print('Por favor, introduzca un número del 1 al 3.')

def procesar_opcion(num):
    if num == 1:
        metodo_1()
    elif num == 2:
        metodo_2()
    elif num == 3:
        print('Finalizando')
        return True  # para indicar que sefinalizar
    else:
        print('Introduzca un número del 1 al 3')
        return False

def metodo_1():
    print('Llamando al método 1')

def metodo_2():
    print('Llamando al método 2')

if __name__ == '__main__':
    main()
