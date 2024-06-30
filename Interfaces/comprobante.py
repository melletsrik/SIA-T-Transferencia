import tkinter as tk

class Comprobante(tk.Frame):
    def __init__(self, master, cuenta, cuenta_origen, cuenta_destino, monto, tipo, nombre_destino=None):
        super().__init__(master)
        self.master = master
        self.cuenta = cuenta
        self.cuenta_origen = cuenta_origen
        self.cuenta_destino = cuenta_destino
        self.monto = monto
        self.tipo = tipo
        self.nombre_destino = nombre_destino
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Comprobante de Transferencia").pack(pady=20)

        if self.tipo == "propia":
            tk.Label(self, text=f"De: {self.cuenta_origen}").pack(pady=5)
            tk.Label(self, text=f"A: {self.cuenta_destino}").pack(pady=5)
        else:
            tk.Label(self, text=f"De: {self.cuenta}").pack(pady=5)
            tk.Label(self, text=f"A: {self.cuenta_destino} ({self.nombre_destino})").pack(pady=5)

        tk.Label(self, text=f"Monto: {self.monto}").pack(pady=5)
        tk.Label(self, text="Transferencia realizada con éxito").pack(pady=20)

        tk.Button(self, text="Finalizar", command=self.finalizar).pack(pady=20)

    def finalizar(self):
        self.master.switch_frame(Menu, self.cuenta)
