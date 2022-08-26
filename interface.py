from tkinter import *
from operations import validate

# Configurations
root = Tk()
root.title("Laboratorio #1. Martin Vega, Tomas Strandgard")
root.geometry("600x300")
#Vars
val_rest1 = StringVar()
val_rest2 = StringVar()
len_ent1 = StringVar()
len_ent2 = StringVar()

# Components
Lb_Title = Label(root, text="Cadenas y simbolos", font='Tahoma, 16')
Fr_Alph_Inp = Frame(root, bg='Yellow')
Lb_Alph_Inp = Label(Fr_Alph_Inp, text="Introduce un alfabeto (sepado por comas)")
Ent_Alph_Imp = Entry(Fr_Alph_Inp)

Fr_Val = Frame(root, bg='Green')
Fr_Inp = Frame(Fr_Val, bg='Red')
Lb_ValInpMsg = Label(Fr_Inp, text='Introduce los textos a verificar')
Ent_Val1 = Entry(Fr_Inp)
Ent_Val2 = Entry(Fr_Inp)

Fr_Outp = Frame(Fr_Val, bg='Blue')
Lb_ValMsg = Label(Fr_Outp, text='Validacion')
Lb_Result1 = Label(Fr_Outp, textvariable=val_rest1)
Lb_Result2 = Label(Fr_Outp, textvariable=val_rest2)

Fr_len = Frame(Fr_Val, bg='Purple')
Lb_lenMsg = Label(Fr_len, text='Caracteres')
Lb_len_rest1 = Label(Fr_len, textvariable=len_ent1)
Lb_len_rest2 = Label(Fr_len, textvariable=len_ent2)

BtmValidate = Button(root,text='Validar')

# Components ubication
Lb_Title.pack()
Fr_Alph_Inp.pack()
Lb_Alph_Inp.pack(side='left', padx='10', expand=True)
Ent_Alph_Imp.pack(side='left', padx='10', expand=True)

Fr_Val.pack(pady='5', fill='both')
Lb_ValInpMsg.pack(expand=True)
Fr_Inp.pack(padx='10', side='left', fill='both', expand=True)
Ent_Val1.pack(fill='x', expand=True)
Ent_Val2.pack(fill='x', expand=True)

Fr_len.pack(side='left', fill='both', expand=True)
Lb_lenMsg.pack(expand=True)
Lb_len_rest1.pack(expand=True)
Lb_len_rest2.pack(expand=True)

Fr_Outp.pack(side='left', fill='both', expand=True)
Lb_ValMsg.pack(expand=True)
Lb_Result1.pack(expand=True)
Lb_Result2.pack(expand=True)

BtmValidate.pack(side='bottom')

######################################################################

# Mapea los resultados y regresa string
def map_result(val):

    if val == 1:
        return 'Correcto' 
    else: 
        return 'Incorrecto'
    
# Coloca la longitud de la cadena
def set_len(ent1, ent2):
    len_ent1.set(len(ent1))
    len_ent2.set(len(ent2))

# Coloca si es correcto o incorrecta la validacion de la cadena
def set_validation(results):
    val_rest1.set(map_result(results[0]))
    val_rest2.set(map_result(results[1]))
    
# Verifica si el alfabeto esta vacio
def alphabet_isNot_empty(text=''):
    if len(text) == 0: 
        print('Vacio')
        return False
    return True
    
def check_inputs():
    # Se obtienen los datos de los inputs
    alphabet = Ent_Alph_Imp.get().strip()
    Ent1 = Ent_Val1.get().strip()
    Ent2 = Ent_Val2.get().strip()

    # Funcion que define la longitud de las cadenas
    set_len(Ent1, Ent2)

    # Verifica si el input del alfabeto no esta vacio
    if alphabet_isNot_empty(alphabet):
        # Invoca la funcion que valida si la cadena coincide con el alfabeto y retorna el resultado
        results = validate(alphabet, Ent1, Ent2)
        # Funcion que muestra los resultados en la interfaz
        set_validation(results)

BtmValidate.config(command=check_inputs)

root.mainloop()


