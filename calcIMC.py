import tkinter as tk

class BMICalculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora de IMC")

        self.weight_label = tk.Label(master, text="Peso (kg):")
        self.weight_entry = tk.Entry(master)
        self.height_label = tk.Label(master, text="Altura (m):")
        self.height_entry = tk.Entry(master)
        self.calculate_button = tk.Button(master, text="Calcular", command=self.calculate_bmi)
        self.result_label = tk.Label(master, text="IMC: ")

        self.weight_label.grid(row=0, column=0)
        self.weight_entry.grid(row=0, column=1)
        self.height_label.grid(row=1, column=0)
        self.height_entry.grid(row=1, column=1)
        self.calculate_button.grid(row=2, columnspan=2)
        self.result_label.grid(row=3, columnspan=2)

    def calculate_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())

            bmi = weight / (height ** 2)

            self.result_label.config(text=f"IMC: {bmi:.2f}")
            self.show_bmi_category(bmi)

        except ValueError:
            tk.messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

    def show_bmi_category(self, bmi):
        if bmi < 18.5:
            category = "Abaixo do peso"
        elif 18.5 <= bmi < 25:
            category = "Peso normal"
        elif 25 <= bmi < 30:
            category = "Sobrepeso"
        else:
            category = "Obesidade"

        category_label = tk.Label(self.master, text=f"Categoria: {category}")
        category_label.grid(row=4, columnspan=2)

root = tk.Tk()
app = BMICalculator(root)
root.mainloop()
