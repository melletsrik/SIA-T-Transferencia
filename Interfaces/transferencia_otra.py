import tkinter as tk
from tkinter import messagebox
from db_connection import connect
from confirmacion import Confirmacion  

class TransferenciaOtra(tk.Frame):
    def __init__(self, master, id_cliente):
        super().__init__(master)
        self.master = master
        self.id_cliente = id_cliente
        self.create_widgets()

    def create_widgets(self):
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT nro_cuenta FROM mae_cuenta WHERE id_cliente = %s", (self.id_cliente,))
        cuentas = cur.fetchall()
        cur.close()
        conn.close()
        
        # Extraer los números de cuenta en una lista
        self.cuentas = [cuenta[0] for cuenta in cuentas]

        tk.Label(self, text="Cuenta Origen:").pack(pady=10)
        self.cuenta_origen_var = tk.StringVar(self)
        self.cuenta_origen_var.set(self.cuentas[0])  # Establecer el primer valor por defecto
        self.cuenta_origen_menu = tk.OptionMenu(self, self.cuenta_origen_var, *self.cuentas)
        self.cuenta_origen_menu.pack(pady=5)

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
        self.master.switch_frame(Menu, self.id_cliente)

    def confirmar(self):
        cuenta_origen = self.cuenta_origen_var.get()
        cuenta_destino = self.cuenta_destino_entry.get()
        monto = self.monto_entry.get()

        if cuenta_destino and monto:
            cuenta_origen = self.cuenta_origen_var.get()
        cuenta_destino = self.cuenta_destino_entry.get()
        monto = self.monto_entry.get()

        if not (cuenta_origen and cuenta_destino and monto):
            messagebox.showerror("Error", "Por favor, complete todos los campos")
            return

        if cuenta_origen == cuenta_destino:
            messagebox.showerror("Error", "La cuenta origen y la cuenta destino no pueden ser iguales")
            return

        try:
            monto = float(monto)
        except ValueError:
            messagebox.showerror("Error", "El monto debe ser un número")
            return

        if monto <= 0:
            messagebox.showerror("Error", "El monto debe ser mayor que cero")
            return

        conn = connect()
        cur = conn.cursor()
        try:
            # Verificar si la cuenta destino existe
            cur.execute("SELECT nro_cuenta FROM mae_cuenta WHERE nro_cuenta = %s", (cuenta_destino,))
            result_destino = cur.fetchone()

            if result_destino is None:
                messagebox.showerror("Error", "La cuenta destino no existe")
                return

            # Obtener el saldo actual de la cuenta origen
            cur.execute("SELECT saldo_actual FROM mae_cuenta WHERE nro_cuenta = %s", (cuenta_origen,))
            result_origen = cur.fetchone()

            if result_origen is None:
                messagebox.showerror("Error", "La cuenta origen no existe")
                return

            saldo_actual = result_origen[0]

            if monto > saldo_actual:
                messagebox.showerror("Error", "El monto excede el saldo actual de la cuenta origen")
                return

            # Obtener el nombre del titular de la cuenta destino
            cur.execute("""
                SELECT mae_persona.nombre, mae_persona.apellido 
                FROM mae_persona
                JOIN mae_cliente ON mae_persona.id_persona = mae_cliente.id_cliente
                JOIN mae_cuenta ON mae_cliente.id_cliente = mae_cuenta.id_cliente
                WHERE mae_cuenta.nro_cuenta = %s
            """, (cuenta_destino,))
            destino = cur.fetchone()

            if destino:
                nombre_destino = f"{destino[0]} {destino[1]}"
                self.master.switch_frame(Confirmacion, self.id_cliente, cuenta_origen, cuenta_destino, monto, "otra", nombre_destino)
            else:
                messagebox.showerror("Error", "No se pudo obtener el nombre del titular de la cuenta destino")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")
        finally:
            cur.close()
            conn.close()