import tkinter as tk
from tkinter import messagebox
from db_connection import connect
from comprobante import Comprobante  # Asegúrate de importar Comprobante

class Confirmacion(tk.Frame):
    def __init__(self, master, id_cliente, cuenta_origen, cuenta_destino, monto, tipo, nombre_destino=None):
        super().__init__(master)
        self.master = master
        self.id_cliente = id_cliente
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
            tk.Label(self, text=f"De: {self.cuenta_origen}").pack(pady=5)
            tk.Label(self, text=f"A: {self.cuenta_destino} ({self.nombre_destino})").pack(pady=5)

        tk.Label(self, text=f"Monto: {self.monto}").pack(pady=5)
        self.itf_label = tk.Label(self, text=f"ITF: {self.calcular_itf(self.monto):.2f}")
        self.itf_label.pack(pady=5)
        tk.Button(self, text="Confirmar", command=self.realizar_transferencia).pack(pady=20)
        tk.Button(self, text="Volver", command=self.volver).pack(pady=10)

    def volver(self):
        if self.tipo == "propia":
            from transferencia_propia import TransferenciaPropia
            self.master.switch_frame(TransferenciaPropia, self.id_cliente)
        elif self.tipo == "otra":
            from transferencia_otra import TransferenciaOtra
            self.master.switch_frame(TransferenciaOtra, self.id_cliente)
        else:
            messagebox.showerror("Error", "Tipo de transferencia no válido")

    def calcular_itf(self, monto):
        return monto * 0.00005 if monto >= 1000 else 0

    def realizar_transferencia(self):
        conn = connect()
        cursor = conn.cursor()
        itf = self.calcular_itf(self.monto)
        try:
            cursor.execute("""
                INSERT INTO trs_transferencia (id_tipo_transferencia, nro_cta_origen, nro_cta_destino, monto, fecha_transferencia, monto_itf) 
                VALUES (%s, %s, %s, %s, CURRENT_DATE, %s)
            """, (1, self.cuenta_origen if self.cuenta_origen else self.id_cliente, self.cuenta_destino, self.monto, itf))
             # Actualizar el saldo de la cuenta origen
            cursor.execute("""
                UPDATE mae_cuenta
                SET saldo_actual = saldo_actual - %s
                WHERE nro_cuenta = %s
            """, (self.monto, self.cuenta_origen if self.cuenta_origen else self.id_cliente))
            
            # Actualizar el saldo de la cuenta destino
            cursor.execute("""
                UPDATE mae_cuenta
                SET saldo_actual = saldo_actual + %s
                WHERE nro_cuenta = %s
            """, (self.monto, self.cuenta_destino))
            
            conn.commit()
            self.master.switch_frame(Comprobante, self.id_cliente, self.cuenta_origen, self.cuenta_destino, self.monto, self.tipo, self.nombre_destino, itf)
        except Exception as e:
            conn.rollback()
            messagebox.showerror("Error", f"Error al realizar la transferencia: {e}")
        finally:
            conn.close()

