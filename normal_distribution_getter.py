#!/usr/bin/env python
# -*-coding: utf-8 -*-
#
# Simulador de calculo de probabilidad
# basandose en una distribucion normal
#
# Eduardo Rivera Geffroy
# 20 Abril, 2023
# al21760177.AT.ite.DOT.edu.Dot.mx

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import numpy as np


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("315x410")  # Previous value: 310x450
        self.title("Calculo de probabilidad")

        # Se inicializa la informacion
        self.media = tk.DoubleVar()
        self.desviacion_estandar = tk.DoubleVar()
        self.valor_minimo = tk.DoubleVar()
        self.valor_maximo = tk.DoubleVar()
        self.tipo_de_calculo = tk.StringVar()
        self.solucion = tk.DoubleVar()
        self.crear_widgets()

    def crear_widgets(self):
        datos = Frame(self)
        datos.pack(fill=tk.X)

        ttk.Label(datos, text="Indique el promedio de los datos", justify=LEFT)\
            .pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        media = Entry(datos, textvariable=self.media)
        media.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

        ttk.Label(datos, text="Indique la desviacion estandar", justify=LEFT) \
            .pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        desviacion = Entry(datos, textvariable=self.desviacion_estandar)
        desviacion.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

        ttk.Label(datos, text="Tipo de calculo a realizar", justify=LEFT) \
            .pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        forma = ttk.Combobox(datos, textvariable=self.tipo_de_calculo,
                             state='readonly', values=["<", "<=", ">", ">=", "a<=x<=b"])
        forma.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        forma.current(0)

        ttk.Label(datos, text="Valor minimo del intervalo", justify=LEFT) \
            .pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        minimo = Entry(datos, textvariable=self.valor_minimo)
        minimo.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

        ttk.Label(datos, text="Valor maximo del intervalo (En caso de que aplique)", justify=LEFT) \
            .pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        maximo = Entry(datos, textvariable=self.valor_maximo)
        maximo.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

        ttk.Button(datos, text="Simular", command=lambda: self.calculo_probabilidad())\
            .pack(side=tk.LEFT, padx=10, pady=5)
        ttk.Button(datos, text="Salir", command=lambda: self.quit())\
            .pack(side=tk.LEFT, padx=10, pady=5)

        solucion = Frame(self)
        solucion.pack(fill=tk.X)
        solucion.config(bg="gray")
        ttk.Label(solucion, text="Probabilidad estimada", justify=LEFT, background="gray")\
            .pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        probabilidad = Entry(solucion, textvariable=self.solucion)
        probabilidad.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

    def validaciones(self):
        if not self.media.get():
            messagebox.showerror("Error de media", "Se debe declarar el promedio de los datos")
            return False

        if not self.desviacion_estandar.get():
            messagebox.showerror("Error de desviacion estanadr", "Se debe declarar el valor de la desviacion estandar")
            return False

        if self.desviacion_estandar.get() <= 0:
            messagebox.showerror("Error de desviacion estanadr", "Valor invalido para la desviacion estandar")
            return False

        if self.tipo_de_calculo.get() == "":
            messagebox.showerror("Error de tipo de problema", "Debe indicar el tipo de calculo a realizar")
            return False

        if not self.valor_minimo.get():
            messagebox.showerror("Falta valor minimo", "Debe indicar el valor minimo del problema")
            return False

        if self.tipo_de_calculo.get() == 'a<=x<=b':
            if not self.valor_maximo.get():
                messagebox.showerror("Falta valor maximo", "Debe indicar el valor maximo del problema al usar a<=x<=b")
                return False

            if self.valor_minimo.get() >= self.valor_maximo.get():
                messagebox.showerror("Error logico", "El valor minimo debe ser menor al valor maximo")
                return False

        return True

    def calculo_probabilidad(self):
        is_valores_validos = self.validaciones()
        if is_valores_validos:
            CANTIDAD_TOTAL_VALORES = 1800
            cantidad_numeros_validos = 0
            valores_aleatorios = np.random.normal(self.media.get(), self.desviacion_estandar.get(), (5, 12, 30))

            for anio in valores_aleatorios:
                for mes in anio:
                    for dia in mes:
                        if self.tipo_de_calculo.get() == '<':
                            if dia < self.valor_minimo.get():
                                cantidad_numeros_validos += 1

                        if self.tipo_de_calculo.get() == '<=':
                            if dia <= self.valor_minimo.get():
                                cantidad_numeros_validos += 1

                        if self.tipo_de_calculo.get() == '>':
                            if dia > self.valor_minimo.get():
                                cantidad_numeros_validos += 1

                        if self.tipo_de_calculo.get() == '>=':
                            if dia >= self.valor_minimo.get():
                                cantidad_numeros_validos += 1

                        if self.tipo_de_calculo.get() == 'a<=x<=b':
                            if self.valor_minimo.get() < dia < self.valor_maximo.get():
                                cantidad_numeros_validos += 1

            print(cantidad_numeros_validos)
            print(cantidad_numeros_validos / CANTIDAD_TOTAL_VALORES)
            self.solucion.set(cantidad_numeros_validos / CANTIDAD_TOTAL_VALORES)


if __name__ == '__main__':
    app = App()
    app.mainloop()
