import tkinter as tk
from tkinter import ttk
def init_window():
    window = tk.Tk()
    window.title('Calculadora')
    window.geometry('600x200')

    label = tk.Label(window, text ='Calculadora', font=('Arial bold', 15))
    label.grid(column = 0, row = 0)

    entrada1 = tk.Entry(window, width=10)
    entrada2 = tk.Entry(window, width=10)

    entrada1.grid(column = 1, row = 1)
    entrada2.grid(column=1, row= 2)

    label_entrada1 = tk.Label(window, text = 'Ingrese primer numero', font=('Arial bold', 10))
    label_entrada1.grid(column = 0, row = 1)

    label_entrada2 = tk.Label(window, text='Ingrese segundo numero', font=('Arial bold', 10))
    label_entrada2.grid(column = 0, row = 1)

    label_operador = tk.Label(window, text = 'Escoja un operador', font=('Arial bold', 10))
    label_operador.grid(column = 0, row = 3)

    combo_operadores = ttk.Combobox(window)
    combo_operadores['values'] = ['+', '-','*', '/', 'pow']
    combo_operadores.current(0)
    combo_operadores.grid(column = 1, row= 3)


    label_resultado = tk.Label(window, text='Resultado: ', font=('Arial bold', 15))
    label_resultado.grid(column = 0, row = 5)



    boton_1 = tk.Button(window,
                        command=lambda: click_negativo(
                            label_resultado,
                            entrada1.get(),
                            entrada2.get(),
                            combo_operadores.get()),
                        text='Cambiar de signo',
                        bg="black",
                        fg="white")
    boton_1.grid(column=2, row=4)

    boton = tk.Button(window,
                      command = lambda: click_calcular(
                                 label_resultado,
                                 entrada1.get(),
                                 entrada2.get(),
                                 combo_operadores.get()),
                      text= 'Calcular',
                      bg="blue",
                      fg="white")
    boton.grid(column = 1, row= 4)

    boton_2 = tk.Button(window,
                        command=lambda: click_entero(
                            label_resultado,
                            entrada1.get(),
                            entrada2.get(),
                            combo_operadores.get()),
                        text = 'Parte entera',
                        bg = "yellow",
                        fg = "black")
    boton_2.grid(column=3, row=4)

    boton_3 = tk.Button(window,
                        command=lambda: click_decimal(
                            label_resultado,
                            entrada1.get(),
                            entrada2.get(),
                            combo_operadores.get()),
                        text='Parte decimal',
                        bg="purple",
                        fg="white")
    boton_3.grid(column=4, row=4)


    window.mainloop ()
def calculadora(num1, num2, operador):
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        resultado = round(num1 / num2, 2)
    else:
        resultado = num1  ** num2
    return resultado
def click_calcular(label, num1, num2, operador):
    valor1 = float(num1)
    valor2 = float(num2)

    res = calculadora(valor1, valor2, operador)

    label.configure(text = 'Resultado: ' + str(res))
def click_negativo(label, num1, num2, operador):
    valor1 = float(num1)
    valor2 = float(num2)
    res = -1 * calculadora(valor1, valor2, operador)

    label.configure(text='Resultado con signo contrario: ' + str(res))
def click_entero(label, num1, num2, operador):
    valor1 = float(num1)
    valor2 = float(num2)
    res = int(calculadora(valor1, valor2, operador))

    label.configure(text='Parte entera: ' + str(res))

def click_decimal(label, num1, num2, operador):
    valor1 = float(num1)
    valor2 = float(num2)
    res = calculadora(valor1, valor2, operador) -  int(calculadora(valor1, valor2, operador))

    label.configure(text='Parte decimal: ' + str(res))
def main():
    init_window()

main()