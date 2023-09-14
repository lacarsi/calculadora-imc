import tkinter as tk
from tkinter import messagebox

# Função para calcular o IMC
def calcular_imc():
    try:
        altura = float(altura_entry.get())
        peso = float(peso_entry.get())
        imc = peso / (altura ** 2)
        imc_int = int(imc)
        resultado_label.config(text=f"IMC: {imc_int}")

        # Classificação do IMC
        if imc < 18.5:
            classificacao_label.config(text="Abaixo do peso")
        elif 18.5 <= imc < 24.9:
            classificacao_label.config(text="Peso normal")
        elif 25 <= imc < 29.9:
            classificacao_label.config(text="Sobrepeso")
        else:
            classificacao_label.config(text="Obesidade")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos para altura e peso.")

# Configuração da janela
window = tk.Tk()
window.title("Calculadora de IMC")

# Entradas de altura e peso
altura_label = tk.Label(window, text="Altura (metros):")
altura_label.pack()
altura_entry = tk.Entry(window)
altura_entry.pack()

peso_label = tk.Label(window, text="Peso (quilogramas):")
peso_label.pack()
peso_entry = tk.Entry(window)
peso_entry.pack()

calcular_button = tk.Button(window, text="Calcular IMC", command=calcular_imc)
calcular_button.pack()

resultado_label = tk.Label(window, text="")
resultado_label.pack()

classificacao_label = tk.Label(window, text="")
classificacao_label.pack()

window.mainloop()
