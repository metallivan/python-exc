# def print_messages():
#     print('Mensaje especial: ')
#     print('¡Estoy aprendiendo a usar Python 👌!')

# print_messages()

def saludar(opt):
    print('Hola')
    print('Como estás')
    print('Elegiste la opción ' + str(opt))
    print('Adios')


opcion = int(input('Elige una opcion (1, 2, 3): '))

if opcion == 1 or opcion == 2 or opcion == 3 :
    saludar(opcion)
else:
    print('Escribe la opcion correcta')

