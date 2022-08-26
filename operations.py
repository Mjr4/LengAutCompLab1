
def conv_alph_to_list(str_alphabet=''):
    list_alphabet = str_alphabet.split(',')
    return list_alphabet

def validate(alph='', ent1='', ent2=''):
    # Convierte el alfabeto a una lista
    alphabet = conv_alph_to_list(alph)
    # Crear una lista con las entradas a validar
    list_of_validates = [ent1, ent2]
    ValidationList = []
    # Ciclo para cada entrada a validar
    for entries in list_of_validates:
        isValid = True
        # ciclo para cada caracter dentro de las entradas a validar
        for character in entries:
            # Si encuentra que un caracter no pertence al alfabeto
            # Cambia la variable isValid y rompe el ciclo
            if character not in alphabet:
                isValid = False
                break
        # Añade a una lista de validaciones los resultados True o False (0,1)
        ValidationList.append(isValid)
    # Retorna el valor de la lista
    return ValidationList

def main():
    print(validate('a,b,c', 'aaaaaaaa', 'abbb', 'axc'))

if __name__ == '__main__':
    main()