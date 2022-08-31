from tkinter import *
from tkinter import messagebox, Radiobutton
from operations import validate, concatenate, ALPHABET


# Configurations
root = Tk()
root.title("Laboratorio")
root.geometry("600x300")
#Vars
val_rest1 = StringVar()
val_rest2 = StringVar()
StrV_ent1 = StringVar()
StrV_ent2 = StringVar()
alphabey = StringVar()
alphabey.set(','.join(ALPHABET))
StrV_ConcRuslt = StringVar()

conc_Opt = IntVar()
# Components
Lb_Title = Label(root, text="Cadenas y simbolos", font='Tahoma, 16')
Fr_Alph_Inp = Frame(root)
Lb_Alph_Inp = Label(Fr_Alph_Inp, text="Alfabeto utilizado")
Ent_Alph_Imp = Entry(Fr_Alph_Inp, state='disabled', textvariable=alphabey)


Fr_Val = Frame(root)
Fr_Inp = Frame(Fr_Val)
Lb_ValInpMsg = Label(Fr_Inp, text='Introduce los textos a verificar')
Ent_Val1 = Entry(Fr_Inp)
Ent_Val2 = Entry(Fr_Inp)

Fr_Outp = Frame(Fr_Val)
Lb_ValMsg = Label(Fr_Outp, text='Validacion')
Lb_Result1 = Label(Fr_Outp, textvariable=val_rest1)
Lb_Result2 = Label(Fr_Outp, textvariable=val_rest2)

Fr_len = Frame(Fr_Val)
Lb_lenMsg = Label(Fr_len, text='Caracteres')
Lb_len_rest1 = Label(Fr_len, textvariable=StrV_ent1)
Lb_len_rest2 = Label(Fr_len, textvariable=StrV_ent2)

Fr_Conc = Frame(root)
Rb_ab = Radiobutton(Fr_Conc, text='AB',variable=conc_Opt, value=0)
Rb_ba = Radiobutton(Fr_Conc, text='BA',variable=conc_Opt, value=1)
Rb_alb = Radiobutton(Fr_Conc, text='AlB',variable=conc_Opt, value=2)
Rb_bla = Radiobutton(Fr_Conc, text='BlA',variable=conc_Opt, value=3)
Btm_Conc = Button(Fr_Conc, text='Concatenar')

Lb_conctResult = Label(root, textvariable=StrV_ConcRuslt)

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

Fr_Conc.pack()
Rb_ab.pack(side='left')
Rb_ba.pack(side='left')
Rb_alb.pack(side='left')
Rb_bla.pack(side='left')
Btm_Conc.pack(side='left')

Lb_conctResult.pack()
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
    StrV_ent1.set(ent1)
    StrV_ent2.set(ent2)


def check_len(ent1, ent2):
    len_Ent1 = len(ent1)
    len_Ent2 = len(ent2)
    if len_Ent1 == 0 or len_Ent2 == 0:
        return False
    set_len(len_Ent1, len_Ent2)
    return True

# Coloca si es correcto o incorrecta la validacion de la cadena
def set_validation(results):
    val_rest1.set(map_result(results[0]))
    val_rest2.set(map_result(results[1]))
    
def check_inputs():
    # Se obtienen los datos de los inputs
    Ent1 = Ent_Val1.get()
    Ent2 = Ent_Val2.get()

    # Verifica si se han introducido cadenas para validar
    if check_len(Ent1, Ent2):
        # Invoca la funcion que valida si la cadena coincide con el alfabeto y retorna el resultado
        results = validate(Ent1, Ent2)
        # Funcion que muestra los resultados en la interfaz
        set_validation(results)
    else:
        messagebox.showwarning('Aviso', 'Introduce cadenas válidas')        


def conc_result():
    # Obtener la opcion de concatenar
    concResult = ''
    a = Ent_Val1.get()
    b = Ent_Val2.get()
    operation = {
        0: concatenate(a,b,False),
        1: concatenate(b,a,False),
        2: concatenate(a,b,True),
        3: concatenate(b,a,True)
    }
    StrV_ConcRuslt.set(operation.get(conc_Opt.get()))


BtmValidate.config(command=check_inputs)
Btm_Conc.config(command=conc_result)
root.mainloop()


