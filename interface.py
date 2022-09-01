from tkinter import *
from tkinter import messagebox, Radiobutton
from operations import validate, concatenate, ALPHABET


# Configurations
root = Tk()
root.title("Laboratorio 1 - Martin Vega, Tomas Strandgard")
root.geometry("600x320")
#Vars
StrV_ReslVal1 = StringVar()
StrV_ReslVal2 = StringVar()
StrV_ent1 = StringVar()
StrV_ent2 = StringVar()
StrV_alphabet = StringVar()
StrV_alphabet.set(','.join(ALPHABET))
StrV_ReslConc = StringVar()
StrV_ReslValExp1 = StringVar()
StrV_ReslValExp2 = StringVar()
conc_Opt = IntVar()


# Components
Lb_Title = Label(root, text="CADENAS Y SIMBOLOS", font='Tahoma, 16')
Fr_Alph_Inp = Frame(root)
Lb_Alph_Inp = Label(Fr_Alph_Inp, text="Alfabeto utilizado")
Ent_Alph_Imp = Entry(Fr_Alph_Inp, state='disabled', textvariable=StrV_alphabet)

Fr_Val = Frame(root)
Fr_Inp = Frame(Fr_Val)
Lb_ValInpMsg = Label(Fr_Inp, text='Introduce los textos a verificar')
Ent_Val1 = Entry(Fr_Inp)
Ent_Val2 = Entry(Fr_Inp)

Fr_Outp = Frame(Fr_Val)
Lb_ValMsg = Label(Fr_Outp, text='Validacion')
Lb_Result1 = Label(Fr_Outp, textvariable=StrV_ReslVal1)
Lb_Result2 = Label(Fr_Outp, textvariable=StrV_ReslVal2)

Fr_len = Frame(Fr_Val)
Lb_lenMsg = Label(Fr_len, text='Caracteres')
Lb_len_rest1 = Label(Fr_len, textvariable=StrV_ent1)
Lb_len_rest2 = Label(Fr_len, textvariable=StrV_ent2)

Btm_validate = Button(Fr_Val,text='Validar')

Fr_Conc = Frame(root)
Fr_ConctImpt = Frame(Fr_Conc)
Rb_ab = Radiobutton(Fr_ConctImpt, text='AB',variable=conc_Opt, value=0)
Rb_ba = Radiobutton(Fr_ConctImpt, text='BA',variable=conc_Opt, value=1)
Rb_alb = Radiobutton(Fr_ConctImpt, text='AlB',variable=conc_Opt, value=2)
Rb_bla = Radiobutton(Fr_ConctImpt, text='BlA',variable=conc_Opt, value=3)
Btm_Conc = Button(Fr_ConctImpt, text='Concatenar')

Lb_conctResult = Label(Fr_Conc, textvariable=StrV_ReslConc, relief=SUNKEN)

Fr_CalcExp = Frame(root)
Fr_CalcExpInp = Frame(Fr_CalcExp)
Lb_ExpMesag = Label(Fr_CalcExpInp, text='Introduce un exponente para calcular la potencia')
Ent_Exp = Entry(Fr_CalcExpInp)
Btm_CalcExp = Button(Fr_CalcExpInp, text='Calcular')

Lb_Val1Exp = Label(Fr_CalcExp, textvariable=StrV_ReslValExp1, relief=SUNKEN)
Lb_Val2Exp = Label(Fr_CalcExp, textvariable=StrV_ReslValExp2, relief=SUNKEN)


# Components ubication
Lb_Title.pack(pady=10)
Fr_Alph_Inp.pack()
Lb_Alph_Inp.pack(side='left', padx='10', expand=True)
Ent_Alph_Imp.pack(side='left', padx='10', expand=True)

Fr_Val.pack(pady='5', padx='5', fill='both')
Lb_ValInpMsg.pack(expand=True)
Fr_Inp.pack(side='left', fill='both', expand=True)
Ent_Val1.pack(fill='x', expand=True)
Ent_Val2.pack(fill='x', expand=True)

Fr_len.pack(side='left', fill='both', padx=10)
Lb_lenMsg.pack()
Lb_len_rest1.pack()
Lb_len_rest2.pack()

Fr_Outp.pack(side='left', fill='both', padx=10)
Lb_ValMsg.pack()
Lb_Result1.pack()
Lb_Result2.pack()

Fr_Conc.pack(pady=10, padx=5, expand=True)

Fr_ConctImpt.pack()
Rb_ab.pack(side='left', padx=5, fill='x')
Rb_ba.pack(side='left', padx=5, fill='x')
Rb_alb.pack(side='left', padx=5, fill='x')
Rb_bla.pack(side='left', padx=5, fill='x')
Btm_Conc.pack(side='left', padx=5, fill='x')

Lb_conctResult.pack(fill='x', expand=True, pady=2)
Btm_validate.pack(expand=True, fill='y')

Fr_CalcExp.pack(pady=10)
Fr_CalcExpInp.pack()
Lb_ExpMesag.pack(side='left', padx=5)
Ent_Exp.pack(side='left', padx=5)
Btm_CalcExp.pack(side='left', padx=5)

Lb_Val1Exp.pack(expand=True, fill='x', pady=2)
Lb_Val2Exp.pack(expand=True, fill='x', pady=2)
######################################################################

# Mapea los resultados y regresa string
def map_result(val):
    if val == 1:
        return 'Correcto' 
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
    return True

# Coloca si es correcto o incorrecta la validacion de la cadena
def set_validation(results):
    StrV_ReslVal1.set(map_result(results[0]))
    StrV_ReslVal2.set(map_result(results[1]))
    
def check_inputs():
    # Se obtienen los datos de los inputs
    Ent1 = Ent_Val1.get()
    Ent2 = Ent_Val2.get()

    # Verifica si se han introducido cadenas para validar
    if check_len(Ent1, Ent2):
        # Coloca el largo de la cadena
        set_len(len(Ent1), len(Ent2))
        # Invoca la funcion que valida si la cadena coincide con el alfabeto y retorna el resultado
        results = validate(Ent1, Ent2)
        # Funcion que muestra los resultados en la interfaz
        set_validation(results)
    else:
        messagebox.showwarning('Aviso', 'Introduce cadenas válidas')        

def conc_result():
    # Obtiene las cadenas
    a = Ent_Val1.get()
    b = Ent_Val2.get()
    operation = {
        0: concatenate(a,b,False),
        1: concatenate(b,a,False),
        2: concatenate(a,b,True),
        3: concatenate(b,a,True)
    }
    # Obtiene la operacion de concatenacion seleccionada
    opSelect = conc_Opt.get()
    # Ejecuta la concatenacion y muestra el resultado
    StrV_ReslConc.set(operation.get(opSelect))

# Potencia de cadenas
def exp_result():
    # Obtiene el exponente
    exp = Ent_Exp.get()
    if not exp.isnumeric() and not len(exp)>0:
        messagebox.showwarning('Alerta', 'Introduce un valor valido')
        return
    exp = int(Ent_Exp.get())
    if exp > 10 or exp <= 0: 
        messagebox.showinfo('Info', 'Valor fuera de rango')
        return
    # Muestra los resultados
    StrV_ReslValExp1.set(Ent_Val1.get()*exp)
    StrV_ReslValExp2.set(Ent_Val2.get()*exp)

Btm_validate.config(command=check_inputs)
Btm_Conc.config(command=conc_result)
Btm_CalcExp.config(command=exp_result)
root.mainloop()


