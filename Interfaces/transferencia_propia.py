import tkinter as tk
from tkinter import messagebox
from confirmacion import Confirmacion  # Asegúrate de importar Confirmacion
from db_connection import connect

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
        tk.Button(self, text="Volver al Menú", command=self.volver_menu).pack(pady=10)

    def volver_menu(self):
        from menu import Menu
        self.master.switch_frame(Menu, self.cuenta)

    def confirmar(self):
        """ cuenta_origen = self.cuenta_origen_entry.get()
        cuenta_destino = self.cuenta_destino_entry.get()
        monto = self.monto_entry.get()

        if cuenta_origen and cuenta_destino and monto:
            self.master.switch_frame(Confirmacion, self.cuenta, cuenta_origen, cuenta_destino, monto, "propia")
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos")"""
        cuenta_origen = self.cuenta_origen_entry.get() 
        cuenta_destino = self.cuenta_destino_entry.get()
        monto = self.monto_entry.get()

        if not (cuenta_origen and cuenta_destino and monto):
            messagebox.showerror("Error", "Por favor, complete todos los campos")
            return

        # Validar que el monto sea un número
        try:
            monto = float(monto)
        except ValueError:
            messagebox.showerror("Error", "El monto debe ser un número")
            return

        # Validar que el monto sea mayor que cero
        if monto <= 0:
            messagebox.showerror("Error", "El monto debe ser mayor que cero")
            return

        # Obtener el saldo actual de la cuenta origen desde la base de datos
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT saldo_actual FROM mae_cuenta WHERE nro_cuenta = %s", (cuenta_origen,))
        result = cur.fetchone()

        if result is None:
            messagebox.showerror("Error", "La cuenta origen no existe")
            return

        saldo_actual = result[0]

        # Verificar si la cuenta destino existe
        cur.execute("SELECT nro_cuenta FROM mae_cuenta WHERE nro_cuenta = %s", (cuenta_destino,))
        result_destino = cur.fetchone()
        cur.close()
        conn.close()
        if result_destino is None:
            messagebox.showerror("Error", "La cuenta destino no existe")
            cur.close()
            conn.close()
            return

        # Validar que el monto no exceda el saldo actual de la cuenta origen
        if monto > saldo_actual:
            messagebox.showerror("Error", "El monto excede el saldo actual de la cuenta origen")
            return

        # Si todas las validaciones son exitosas, proceder con la transferencia
        self.master.switch_frame(Confirmacion, self.cuenta, cuenta_origen, cuenta_destino, monto, "propia")
