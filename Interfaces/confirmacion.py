import tkinter as tk
from tkinter import messagebox
from db_connection import connect
from comprobante import Comprobante  # Asegúrate de importar Comprobante

class Confirmacion(tk.Frame):
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
        tk.Label(self, text="Confirmar Transferencia").pack(pady=20)

        if self.tipo == "propia":
            tk.Label(self, text=f"De: {self.cuenta_origen}").pack(pady=5)
            tk.Label(self, text=f"A: {self.cuenta_destino}").pack(pady=5)
        else:
            tk.Label(self, text=f"De: {self.cuenta}").pack(pady=5)
            tk.Label(self, text=f"A: {self.cuenta_destino} ({self.nombre_destino})").pack(pady=5)

        tk.Label(self, text=f"Monto: {self.monto}").pack(pady=5)
        tk.Button(self, text="Confirmar", command=self.realizar_transferencia).pack(pady=20)

    def realizar_transferencia(self):
        conn = connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO trs_transferencia (id_tipo_transferencia, nro_cta_origen, nro_cta_destino, monto, fecha_transferencia) 
                VALUES (%s, %s, %s, %s, CURRENT_DATE)
            """, (1, self.cuenta_origen if self.cuenta_origen else self.cuenta, self.cuenta_destino, self.monto))
            conn.commit()
            self.master.switch_frame(Comprobante, self.cuenta, self.cuenta_origen, self.cuenta_destino, self.monto, self.tipo, self.nombre_destino)
        except Exception as e:
            conn.rollback()
            messagebox.showerror("Error", f"Error al realizar la transferencia: {e}")
        finally:
            conn.close()
