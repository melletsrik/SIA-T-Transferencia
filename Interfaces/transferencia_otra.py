import tkinter as tk
from tkinter import messagebox
from db_connection import connect
from confirmacion import Confirmacion  # Asegúrate de importar Confirmacion

class TransferenciaOtra(tk.Frame):
    def __init__(self, master, cuenta):
        super().__init__(master)
        self.master = master
        self.cuenta = cuenta
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Cuenta Destino:").pack(pady=10)
        self.cuenta_destino_entry = tk.Entry(self)
        self.cuenta_destino_entry.pack(pady=5)

        tk.Label(self, text="Monto:").pack(pady=10)
        self.monto_entry = tk.Entry(self)
        self.monto_entry.pack(pady=5)

        tk.Button(self, text="Siguiente", command=self.confirmar).pack(pady=20)

    def confirmar(self):
        cuenta_destino = self.cuenta_destino_entry.get()
        monto = self.monto_entry.get()

        if cuenta_destino and monto:
            conn = connect()
            cursor = conn.cursor()
            cursor.execute("SELECT nro_cuenta FROM mae_cuenta WHERE id_cliente = %s", (self.cuenta,))
            cuenta_origen = cursor.fetchone()[0]  # Obtenemos directamente el número de cuenta
            cursor.execute("""
                SELECT p.nombre, p.apellido 
                FROM mae_persona p
                JOIN mae_cliente c ON p.id_persona = c.id_cliente
                JOIN mae_cuenta cu ON c.id_cliente = cu.id_cliente
                WHERE cu.nro_cuenta = %s
            """, (cuenta_destino,))
            destino = cursor.fetchone()
            conn.close()

            if destino:
                nombre_destino = f"{destino[0]} {destino[1]}"
                self.master.switch_frame(Confirmacion, self.cuenta, cuenta_origen, cuenta_destino, monto, "otra", nombre_destino)
            else:
                messagebox.showerror("Error", "Cuenta destino no encontrada")
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos")
