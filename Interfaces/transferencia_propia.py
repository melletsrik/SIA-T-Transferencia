import tkinter as tk
from tkinter import messagebox
from confirmacion import Confirmacion  # Asegúrate de importar Confirmacion

class TransferenciaPropia(tk.Frame):
    def __init__(self, master, cuenta):
        super().__init__(master)
        self.master = master
        self.cuenta = cuenta
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Cuenta Origen:").pack(pady=10)
        self.cuenta_origen_entry = tk.Entry(self)
        self.cuenta_origen_entry.pack(pady=5)

        tk.Label(self, text="Cuenta Destino:").pack(pady=10)
        self.cuenta_destino_entry = tk.Entry(self)
        self.cuenta_destino_entry.pack(pady=5)

        tk.Label(self, text="Monto:").pack(pady=10)
        self.monto_entry = tk.Entry(self)
        self.monto_entry.pack(pady=5)

        tk.Button(self, text="Siguiente", command=self.confirmar).pack(pady=20)

    def confirmar(self):
        cuenta_origen = self.cuenta_origen_entry.get()
        cuenta_destino = self.cuenta_destino_entry.get()
        monto = self.monto_entry.get()

        if cuenta_origen and cuenta_destino and monto:
            self.master.switch_frame(Confirmacion, self.cuenta, cuenta_origen, cuenta_destino, monto, "propia")
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos")
