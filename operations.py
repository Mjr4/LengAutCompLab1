ALPHABET = ['a','b','c']

def validate(ent1='', ent2=''):
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
            if character not in ALPHABET:
                isValid = False
                break
        # Añade a una lista de validaciones los resultados True o False (0,1)
        ValidationList.append(isValid)
    # Retorna el valor de la lista
    return ValidationList

def main():
    print(validate('', ''))

if __name__ == '__main__':
    main()