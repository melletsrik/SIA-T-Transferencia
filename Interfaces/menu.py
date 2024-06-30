import tkinter as tk
from transferencia_propia import TransferenciaPropia  # Asegúrate de importar TransferenciaPropia
from transferencia_otra import TransferenciaOtra  # Asegúrate de importar TransferenciaOtra

class Menu(tk.Frame):
    def __init__(self, master, id_cliente):
        super().__init__(master)
        self.master = master
        self.id_cliente = id_cliente
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Menú Principal").pack(pady=20)
        tk.Button(self, text="Transferencia Entre Cuentas Propias", command=self.transferencia_propia).pack(pady=10)
        tk.Button(self, text="Transferencia a Otras Cuentas", command=self.transferencia_otra).pack(pady=10)

    def transferencia_propia(self):
        self.master.switch_frame(TransferenciaPropia, self.id_cliente)

    def transferencia_otra(self):
        self.master.switch_frame(TransferenciaOtra, self.id_cliente)

